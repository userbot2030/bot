
from . import cli
from config import MONGO_URL
from pyrogram.types import Message
from pyrogram import Client, filters
from pymongo import MongoClient
from typing import List


client = MongoClient(MONGO_URL)
cli = client["ubot"]
collection = cli["prefix"]



async def set_prefix(user_id, prefix):
    pref = collection.get(f"user.{user_id}", "prefix", ".")
    if prefix != pref:
        collection.set(f"user.{user_id}", "prefix", prefix)
        return True
    return False


def get_prefix(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        pref = collection.get(f"user.{user_id}", "prefix", ".")
        prefix = pref if pref is not None else ""
        return await func(client, message, prefix)
    return wrapper
