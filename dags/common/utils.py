import logging
import typing

import duckdb


def execute_sql(filename, params: object = None):
    logging.info(f"Executing {filename}...")
    with open(filename, "r") as f:
        duckdb.execute(f.read(), params)


def find_newest_file(files: typing.List[str]) -> str:
    return max(files)
