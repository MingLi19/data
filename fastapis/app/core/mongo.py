from pymongo import MongoClient

from .config import Settings

settings = Settings()

DATABASE_URL = settings.mongo_dsn.unicode_string()


class MongoDBManager:
    def __init__(self):
        self.client = MongoClient(DATABASE_URL)

    def __enter__(self):
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


def get_mondo_db_client():
    with MongoDBManager() as client:
        yield client
