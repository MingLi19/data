from fastapi import Depends
from pymongo import MongoClient

from app.core.mongo import get_mondo_db_client


def get_data_service(client: MongoClient = Depends(get_mondo_db_client)):
    return DataService(client)


class DataService:
    def __init__(self, client: MongoClient):
        self.v = client

    def get_all_data(self):
        return self.v.list_database_names()
