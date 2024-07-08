import functools

import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):
#     SFTP_URL: str = pydantic.Field(env="SFTP_URL", default="localhost")
#     SFTP_PORT: int = pydantic.Field(env="SFTP_PORT", default=22)

#     SFTP_USERNAME: str = pydantic.Field(env="SFTP_USERNAME", default="admin")
#     SFTP_PASSWORD: str = pydantic.Field(env="SFTP_PASSWORD", default="admin")
#     SFTP_PKEY: str = pydantic.Field(env="SFTP_PKEY", default="/tmp/key.pem")

#     OUTPUT_PATH: str = pydantic.Field(env="OUTPUT_PATH", default="data")


class Settings(pydantic.BaseModel):
    SFTP_URL: str = ""
    SFTP_PORT: int = ""

    SFTP_USERNAME: str = ""
    SFTP_PASSWORD: str = ""
    SFTP_PKEY: str = ""

    OUTPUT_PATH: str = "data/"

    GCP_CONN_ID: str = "google_cloud_default"
    GCS_SRC: str = "sftp_to_gcs"

    PRICE_SEARCH_SFTP_KEYS_GSC: str = "price_search_sftp_keys_gcs"

    SENTIMENT_ANALYSIS_GCS: str = "sentiment_analysis_gcs"
    PRICE_SEARCH_GCS: str = "price_search_gcs"


@functools.lru_cache()
def get_settings() -> Settings:
    return Settings()
