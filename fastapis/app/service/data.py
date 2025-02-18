from fastapi import Depends
from pymongo import MongoClient

from app.core.mongo import get_mondo_db_client


def get_data_service(client: MongoClient = Depends(get_mondo_db_client)):
    return DataService(client)


class DataService:
    def __init__(self, client: MongoClient):
        self.client = client

    def get_all_data(self):
        return self.client.list_database_names()

    def insert_data(self, data):
        # db -> collection -> document
        self.client.db.records.insert_one(data)

    def get_data_by_id(self, data_id):
        return self.client.db.records.find()

    def insert_standard_data(self, data):
        # db -> collection -> StandardData
        self.client.db.StandardData.insert_many(data)
