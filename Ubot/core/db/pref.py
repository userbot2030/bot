
from . import cli
from config import MONGO_URL
from pyrogram.types import Message
from pyrogram import Client, filters
from pymongo import MongoClient
from typing import List


client = MongoClient(MONGO_URL)
cli = client["ubot"]
collection = cli["prefix"]

import pymongo

mongo_client = pymongo.MongoClient(MONGO_URL)
db = mongo_client["mydatabase"]


async def set_prefix(user_id, prefix):
    db_prefix = db.get(f"user.{user_id}", "prefix", ".")
    if prefix != db_prefix:
        db.set(f"user.{user_id}", "prefix", prefix)
        return True
    return False


def get_prefix(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        db_prefix = db.get(f"user.{user_id}", "prefix", ".")
        prefix = db_prefix if db_prefix is not None else ""
        return await func(client, message, prefix)
    return wrapper
