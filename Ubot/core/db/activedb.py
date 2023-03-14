from pyrogram.filters import chat
from . import cli
from typing import Dict, List, Union
from datetime import datetime, timedelta, relativedelta
from .accesdb import *
import schedule
import asyncio
collection = ["expire_date"]



async def get_active_time(user_id):
    expire_date = await get_expired_date(user_id)
    if expire_date:
        active_time = expire_date - datetime.now()
        if active_time.total_seconds() > 0:
            return active_time
        else:
            await delete_user_access(user_id)
            await rem_expired_date(user_id)
            return None
    else:
        return None

File "/root/bot/Ubot/core/db/activedb.py", line 26, in get_expired_date
    user = await collection.users.find_one({"_id": user_id})
AttributeError: 'list' object has no attribute 'users'

async def get_expired_date(user_id):
    user = await collection.users.find_one({"_id": user_id})
    if user:
        expire_date = user.get("expire_date")
        if expire_date:
            return expire_date
        else:
            return None
    else:
        return None

async def rem_expired_date(user_id):
    await collection.users.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )

async def remove_expired():
    async for user in collection.users.find({"expire_date": {"$lt": datetime.now()}}):
        await delete_user_access(user["_id"])
        await rem_expired_date(user["_id"])


async def set_expired_date(user_id, active_time):
    if active_time == 1:
        expire_date = datetime.now() + relativedelta(months=1)
    else:
        expire_date = datetime.now() + timedelta(days=30)
    collection.users.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True)
    schedule.every().day.at("00:00").do(remove_expired)
    asyncio.create_task(schedule_loop())


async def schedule_loop():
    while True:
        await asyncio.sleep(1)
        schedule.run_pending()
