
from . import cli
from typing import List

collection = cli["prefix"]



async def get_prefix(user_id: int) -> str:
    result = await collection.find_one({"user_id": user_id})
    if result is None:
        return None
    else:
        return result["prefix"]


async def set_prefix(user_id: int, prefix: str) -> None:
    await collection.update_one({"user_id": user_id}, {"$set": {"prefix": prefix}}, upsert=True)


async def get_users_with_prefix() -> List[int]:
    results = await collection.find({"prefix": {"$ne": ""}})
    return [result["user_id"] for result in results]
