from pyrogram.filters import chat
from pyrogram import Client
from . import cli
from .activedb import set_expired_date
from typing import Dict, List, Union
from datetime import datetime, timedelta
import pymongo.errors
from Ubot.modules.basic import ADMINS


collection = cli["access"]


async def grant_access(user_id: int) -> bool:
    access = {"user_id": user_id}
    try:
        result = await collection.users.update_one(
            {'user_id': user_id},
            {'$set': {'user_id': user_id}},
            upsert=True
        )
        if result.upserted_id or result.modified_count:
            return True
        else:
            return False
    except pymongo.errors.PyMongoError:
        return False
        

async def get_users_access() -> List[str]:
    try:
        cursor = collection.users.find({}, {'access_list': 1})
        users_access = set()
        async for document in cursor:
            if 'access_list' in document:
                users_access.update(document['access_list'])
        return list(users_access)
    except pymongo.errors.PyMongoError:
        return []


async def revoke_access(user_id: int) -> bool:
    try:
        user = await collection.users.find_one({'user_id': user_id})
        if user is not None and user.get('banned'):
            return False
        result = await collection.users.update_one(
            {'user_id': user_id},
            {'$set': {'banned': True}},
            upsert=True
        )
        if result.upserted_id:
            return False
        elif result.matched_count > 0 or result.modified_count > 0:
            return True
        else:
            return False
    except pymongo.errors.PyMongoError:
        return False


async def check_user_access(user_id: int) -> bool:
    access = {"user_id": user_id}
    result = await collection.users.find_one(access)
    if result:
        return True
    else:
        return False
        
async def delete_user_access(user_id: int) -> bool:
    try:
        result = await collection.users.delete_one({'user_id': user_id})
        if result.deleted_count > 0:
            return True
        else:
            return False
    except pymongo.errors.PyMongoError:
        return False

def check_access(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        user_access = await check_user_access(user_id)
        if user_id not in ADMINS and not user_access:
            await message.reply_text("Maaf, Anda tidak memiliki akses untuk menggunakan bot ini.\n Silakan ke @kynansupport untuk mendapatkan akses dari Admin disana.")
            return
        await func(client, message)
    return wrapper



async def check_and_grant_user_access(user_id: int, duration: int) -> None:
    if await check_user_access(user_id):
        await delete_user_access(user_id)
    if await grant_access(user_id) and await set_expired_date(user_id, duration):
        return
    else:
        await delete_user_access(user_id)

