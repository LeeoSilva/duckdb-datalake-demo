FROM apache/airflow:2.9.2
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir diagrams apache-airflow==2.9.2 paramiko pydantic pydantic-settings sftpserver apache-airflow[google] duckdb


# copy .env
COPY .env /opt/airflow/.env
