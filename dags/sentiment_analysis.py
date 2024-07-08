import datetime
import logging

import duckdb
from airflow.decorators import dag, task
from common.settings import get_settings
from common.utils import execute_sql
from services.sentiment_analysis import SentimentAnalysisService

from dags.common.gsc import write_to_gcs


@dag(
    schedule_interval="0 0 * * *",
    start_date=datetime.datetime(2022, 1, 1),
    catchup=False,
)
def sentiment_analysis():
    @task
    def prepare_tables():
        logging.info("Preparing Tables")

        duckdb_conn = duckdb.connect(":memory:")

        sql_files = (
            "sql/create_products.sql",
            "sql/create_sentiment_status.sql",
            "sql/create_source.sql",
            "sql/create_sentiment_analysis_fact.sql",
        )

        for sql in sql_files:
            logging.info(f"Executing {sql}...")
            execute_sql(sql)

    @task
    def extract():
        logging.info("Extracting Sentiment Analysis...")
        sentiment_analysis_service = SentimentAnalysisService()

        comments = sentiment_analysis_service.get_comments()

        write_to_gcs(comments)

    @task
    def transform():
        logging.info("Transforming data...")
        duckdb.connect(":memory:")

        # Getting the data directly from GCS
        sentiment_analysis_storage = get_settings().SENTIMENT_ANALYSIS_GCS
        duckdb.execute("sql/extract_sentiment_analysis.sql", sentiment_analysis_storage)

        # Transform the data
        duckdb.sql("sql/transform_sentiment_analysis.sql")

    @task
    def load():
        logging.info("Loading data...")

        duckdb.connect(":memory:")

        # Write the data to the GC Storage in parquet format.
        duckdb.execute("sql/load_sentiment_analysis.sql")

    prepare_tables_task = prepare_tables()
    extract_task = extract()
    transform_task = transform()
    load_task = load()

    prepare_tables_task >> extract_task >> transform_task >> load_task


sentiment_analysis()
