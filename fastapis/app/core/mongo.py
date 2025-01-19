from pymongo import MongoClient

from .config import Settings

settings = Settings()

DATABASE_URL = settings.mongo_dsn.unicode_string()

if DATABASE_URL is not None:
    mongodb_client = MongoClient(DATABASE_URL)
else:
    raise ValueError("Database URL is not provided.")


class MongoDBManager:
    def __init__(self):
        self.client = mongodb_client

    def __enter__(self):
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


def get_mondo_db_client():
    with MongoDBManager() as client:
        yield client
