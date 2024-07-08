import datetime
import logging
import os

import duckdb
from airflow.decorators import dag, task
from airflow.providers.google.cloud.transfers.sftp_to_gcs import SFTPToGCSOperator
from common.gsc import download_sftp_keys, write_to_gcs
from common.settings import get_settings
from common.utils import execute_sql
from services.price_search_sftp import PriceSearchSFTPService


@dag(
    schedule_interval="0 0 * * *",
    start_date=datetime.datetime(2022, 1, 1),
    catchup=False,
)
def price_search():

    @task
    def prepare_tables():
        logging.info("Preparing Tables")
        duckdb_conn = duckdb.connect(":memory:")

        sql_files = (
            "sql/create_products.sql",
            "sql/create_stores.sql",
            "sql/create_stock_control.sql",
            "sql/create_customers.sql",
            "sql/create_price_search_fact.sql",
        )

        for sql in sql_files:
            logging.info(f"Executing {sql}...")
            execute_sql(sql)

    @task
    def prepare_sftp_keys():
        logging.info("Downloading SFTP keys...")

        # Download the SFTP keys from GCS
        sftp_keys_storage = get_settings().PRICE_SEARCH_SFTP_KEYS_GSC

        # Download the keys
        download_sftp_keys(sftp_keys_storage)

    @task
    def extract():
        logging.info("Extracting Sentiment Analysis...")

        price_search = PriceSearchSFTPService()
        prices = price_search.download_files()

        write_to_gcs(prices)

    @task
    def transform():
        logging.info("Transforming data...")
        duckdb.connect(":memory:")

        # Getting the data directly from GCS
        price_search_storage = get_settings().PRICE_SEARCH_GCS
        duckdb.execute("sql/extract_price_search.sql", price_search_storage)

        # Transform the data
        duckdb.sql("sql/transform_price_search.sql")

    @task
    def load():
        logging.info("Loading data...")

        duckdb.connect(":memory:")

        # Write the data to the GC Storage in parquet format.
        duckdb.execute("sql/load_price_search.sql")

    copy_sftp_to_gcs_task = SFTPToGCSOperator(
        task_id="extract_from_sftp",
        sftp_conn_id=get_settings().SFTP_CONN_ID,
        gcp_conn_id=get_settings().GCP_CONN_ID,
        source_path=os.path.join(get_settings().OUTPUT_PATH, "*.csv"),
        destination_bucket=get_settings().GCS_SRC,
    )

    prepare_tables_task = prepare_tables()
    extract_task = extract()
    transform_task = transform()
    load_task = load()

    (
        prepare_sftp_keys
        >> prepare_tables_task
        >> copy_sftp_to_gcs_task
        >> extract_task
        >> transform_task
        >> load_task,
    )


price_search()
