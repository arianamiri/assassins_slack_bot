import os

from contextlib2 import contextmanager
import pymysql


_DB_HOST = os.environ['DB_HOST']
_DB_PORT = int(os.environ['DB_PORT'])
_DB_NAME = os.environ['DB_NAME']
_DB_USER = os.environ['DB_USERNAME']
_DB_PASSWORD = os.environ['DB_PASSWORD']


connection = pymysql.connect(
    host=_DB_HOST,
    port=_DB_PORT,
    database=_DB_NAME,
    user=_DB_USER,
    password=_DB_PASSWORD
)


@contextmanager
def db_transaction():
    try:
        yield
    except Exception:
        connection.rollback()
    else:
        connection.commit()
