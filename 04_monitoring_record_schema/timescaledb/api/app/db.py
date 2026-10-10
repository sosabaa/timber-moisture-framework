import os

import psycopg
from psycopg.rows import dict_row


def connect() -> psycopg.Connection:
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("POSTGRES_DB", "timber_moisture"),
        user=os.getenv("POSTGRES_USER", "tmf_app"),
        password=os.environ["POSTGRES_PASSWORD"],
        row_factory=dict_row,
    )

