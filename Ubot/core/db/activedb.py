from pyrogram.filters import chat
from . import cli
from typing import Dict, List, Union
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from .accesdb import *
import schedule
import asyncio
collection = cli["active"]



async def get_expired_date(user_id):
    user = await collection.users.find_one({"_id": user_id})
    if user:
        expire_date = user.get("expire_date")
        if expire_date:
            remaining_days = (expire_date - datetime.now()).days
            remaining_days = (datetime.now() + timedelta(days=remaining_days)).strftime('%d-%m-%Y')
            return remaining_days
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


async def set_expired_date(user_id, duration):
    days_in_month = 30
    if duration <= 12:
        days_in_month = 30 * duration
    expire_date = datetime.now() + timedelta(days=days_in_month)
    collection.users.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True)
    schedule.every().day.at("00:00").do(remove_expired)
    asyncio.create_task(schedule_loop())



async def schedule_loop():
    while True:
        await asyncio.sleep(1)
        schedule.run_pending()
