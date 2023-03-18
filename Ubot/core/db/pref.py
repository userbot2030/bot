
from . import cli
from config import MONGO_URL
from pymongo import MongoClient
from typing import List


client = MongoClient(MONGO_URL)
cli = client["ubot"]

collection = cli["prefix"]





async def get_prefix(user_id: int) -> str:
    result = await collection.find_one({"user_id": user_id})
    if result is None:
        return None
    else:
        return result.get("prefix", "")


async def set_prefix(user_id: int, prefix: str) -> None:
    collection.update_one({"user_id": user_id}, {"$set": {"prefix": prefix}}, upsert=True)


async def get_users_with_prefix() -> List[int]:
    results = await collection.find({"prefix": {"$ne": ""}})
    return [result["user_id"] for result in results]

prefix = get_prefix(user_id)