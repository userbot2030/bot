import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from config import MONGO_URL
from Ubot.confing import get_int_key, get_str_key


MONGO_PORT = get_int_key("27017")
MONGO_URL = get_str_key("MONGO_URL")
MONGO_DB = "ubot"


client = MongoClient()
client = MongoClient(MONGO_URL, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_URL, MONGO_PORT)
db = motor[MONGO_DB]
db = client["ubot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
