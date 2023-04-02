
"""
import json
import threading
import dns.resolver
import pymongo
import sqlite3
from config import MONGO_URL, DB_NAME


db_name = DB_NAME
db_url = MONGO_URL

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ["8.8.8.8"]


class Database:
    def get(self, user_id: str, module: str, variable: str, default=None):
        """Get value from database"""
        raise NotImplementedError

    def set(self, user_id: str, module: str, variable: str, value):
        """Set key in database"""
        raise NotImplementedError

    def remove(self, user_id: str, module: str, variable: str):
        """Remove key from database"""
        raise NotImplementedError

    def get_collection(self, user_id: str, module: str) -> dict:
        """Get database for selected module"""
        raise NotImplementedError

    def close(self):
        """Close the database"""
        raise NotImplementedError


class MongoDatabase(Database):
    def __init__(self, url, name):
        self._client = pymongo.MongoClient(url)
        self._database = self._client[name]

    def _get_collection(self, user_id: str, module: str):
        return self._database[f"{user_id}_{module}"]

    def set(self, user_id: str, module: str, variable: str, value):
        collection = self._get_collection(user_id, module)
        collection.replace_one(
            {"var": variable}, {"var": variable, "val": value}, upsert=True
        )

    def get(self, user_id: str, module: str, variable: str, expected_value=None):
        collection = self._get_collection(user_id, module)
        doc = collection.find_one({"var": variable})
        return expected_value if doc is None else doc["val"]

    def get_collection(self, user_id: str, module: str):
        collection = self._get_collection(user_id, module)
        return {item["var"]: item["val"] for item in collection.find()}

    def remove(self, user_id: str, module: str, variable: str):
        collection = self._get_collection(user_id, module)
        collection.delete_one({"var": variable})

    def close(self):
        self._client.close()



db = MongoDatabase(db_url, db_name)

"""