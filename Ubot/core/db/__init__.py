
from pyrogram.filters import chat
from pyrogram import Client
from typing import Dict, List, Union
from datetime import datetime, timedelta
import pymongo.errors
from Ubot.modules.basic import ADMINS
from dateutil.relativedelta import relativedelta
from ubotlibs.ubot.database import cli

import schedule
import asyncio
from Ubot import *

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import MONGO_URL

mongo = MongoCli(MONGO_URL)
db = mongo.ubot

coupledb = db.couple
karmadb = db.karma
notesdb = db.notes
accesdb = db.acces
usersdb = db.users


usersdb.update_many({}, {"$set": {"bot_log_group_id": None}})


async def buat_log():
    for bot in bots:
        botlog_chat_id = os.environ.get('BOTLOG_CHATID')
        if not botlog_chat_id:
            user = await bot.get_me()
            user_id = user.id
            user_data = db.users.find_one({"user_id": user_id})
            if user_data:
                botlog_chat_id = user_data.get("bot_log_group_id")

        if not botlog_chat_id:
            group_name = 'Naya Project Bot Log'
            group_description = 'This group is used to log my bot activities'
            group = await bot.create_supergroup(group_name, group_description)
            botlog_chat_id = group.id

            user = await bot.get_me()
            user_id = user.id
            db.users.update_one({"user_id": user_id}, {"$set": {"bot_log_group_id": botlog_chat_id}})

            if await is_heroku():
                try:
                    Heroku = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
                    happ = Heroku.app(os.environ.get('HEROKU_APP_NAME'))
                    happ.config()['BOTLOG_CHATID'] = str(botlog_chat_id)
                except:
                    pass
            else:
                with open('.env', 'a') as env_file:
                    env_file.write(f'\nBOTLOG_CHATID={botlog_chat_id}')

            message_text = 'Group Log Berhasil Dibuat,\n Mohon Masukan Bot @NayaProjectBot Ke Group ini.'
            await bot.send_message(botlog_chat_id, message_text)
            restart()

        message = 'Test log message'
        await bot.send_message(botlog_chat_id, message)



async def grant_access(user_id: int) -> bool:
    access = {"user_id": user_id}
    try:
        result = await accesdb.users.update_one(
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
        cursor = accesdb.users.find({}, {'access_list': 1})
        users_access = set()
        async for document in cursor:
            if 'access_list' in document:
                users_access.update(document['access_list'])
        return list(users_access)
    except pymongo.errors.PyMongoError:
        return []


async def revoke_access(user_id: int) -> bool:
    try:
        user = await accesdb.users.find_one({'user_id': user_id})
        if user is not None and user.get('banned'):
            return False
        result = await accesdb.users.update_one(
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
    result = await accesdb.users.find_one(access)
    if result:
        return True
    else:
        return False
        
async def delete_user_access(user_id: int) -> bool:
    try:
        result = await accesdb.users.delete_one({'user_id': user_id})
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

async def get_expired_date(user_id):
    user = await accesdb.users.find_one({"_id": user_id})
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
    await accesdb.users.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )

async def remove_expired():
    async for user in accesdb.users.find({"expire_date": {"$lt": datetime.now()}}):
        await delete_user_access(user["_id"])
        await rem_expired_date(user["_id"])


async def set_expired_date(user_id, duration):
    days_in_month = 30
    if duration <= 12:
        days_in_month = 30 * duration
    expire_date = datetime.now() + timedelta(days=days_in_month)
    accesdb.users.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True)
    schedule.every().day.at("00:00").do(remove_expired)
    asyncio.create_task(schedule_loop())



async def schedule_loop():
    while True:
        await asyncio.sleep(1)
        schedule.run_pending()

async def check_and_grant_user_access(user_id: int, duration: int) -> None:
    if await check_user_access(user_id):
        await delete_user_access(user_id)
    if await grant_access(user_id) and await set_expired_date(user_id, duration):
        return


async def _get_lovers(chat_id: int):
    lovers = await coupledb.find_one({"chat_id": chat_id})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers


async def get_couple(chat_id: int, date: str):
    lovers = await _get_lovers(chat_id)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(chat_id: int, date: str, couple: dict):
    lovers = await _get_lovers(chat_id)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": chat_id},
        {"$set": {"couple": lovers}},
        upsert=True,
    )


async def get_karmas_count() -> dict:
    chats_count = 0
    karmas_count = 0
    async for chat in karmadb.find({"chat_id": {"$lt": 0}}):
        for i in chat["karma"]:
            karma_ = chat["karma"][i]["karma"]
            if karma_ > 0:
                karmas_count += karma_
        chats_count += 1
    return {"chats_count": chats_count, "karmas_count": karmas_count}


async def user_global_karma(user_id) -> int:
    total_karma = 0
    async for chat in karmadb.find({"chat_id": {"$lt": 0}}):
        karma = await get_karma(chat["chat_id"], await int_to_alpha(user_id))
        if karma and (int(karma["karma"]) > 0):
            total_karma += int(karma["karma"])
    return total_karma


async def get_karmas(chat_id: int) -> Dict[str, int]:
    karma = await karmadb.find_one({"chat_id": chat_id})
    if not karma:
        return {}
    return karma["karma"]


async def get_karma(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    karmas = await get_karmas(chat_id)
    if name in karmas:
        return karmas[name]


async def update_karma(chat_id: int, name: str, karma: dict):
    name = name.lower().strip()
    karmas = await get_karmas(chat_id)
    karmas[name] = karma
    await karmadb.update_one(
        {"chat_id": chat_id}, {"$set": {"karma": karmas}}, upsert=True
    )


async def is_karma_on(chat_id: int) -> bool:
    chat = await karmadb.find_one({"chat_id_toggle": chat_id})
    if not chat:
        return True
    return False


async def karma_on(chat_id: int):
    is_karma = await is_karma_on(chat_id)
    if is_karma:
        return
    return await karmadb.delete_one({"chat_id_toggle": chat_id})


async def karma_off(chat_id: int):
    is_karma = await is_karma_on(chat_id)
    if not is_karma:
        return
    return await karmadb.insert_one({"chat_id_toggle": chat_id})


async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text


async def alpha_to_int(user_id_alphabet: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    user_id = ""
    for i in user_id_alphabet:
        index = alphabet.index(i)
        user_id += str(index)
    user_id = int(user_id)
    return user_id

async def get_notes_count() -> dict:
    chats_count = 0
    notes_count = 0
    async for chat in notesdb.find({"user_id": {"$exists": 1}}):
        notes_name = await get_note_names(chat["user_id"])
        notes_count += len(notes_name)
        chats_count += 1
    return {"chats_count": chats_count, "notes_count": notes_count}


async def _get_notes(user_id: int) -> Dict[str, int]:
    _notes = await notesdb.find_one({"user_id": user_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_note_names(user_id: int) -> List[str]:
    _notes = []
    for note in await _get_notes(user_id):
        _notes.append(note)
    return _notes


async def get_note(user_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_notes(user_id)
    if name in _notes:
        return _notes[name]
    return False


async def save_note(user_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_notes(user_id)
    _notes[name] = note

    await notesdb.update_one(
        {"user_id": user_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_note(user_id: int, name: str) -> bool:
    notesd = await _get_notes(user_id)
    name = name.lower().strip()
    if name in notesd:
        del notesd[name]
        await notesdb.update_one(
            {"user_id": user_id},
            {"$set": {"notes": notesd}},
            upsert=True,
        )
        return True
    return False


