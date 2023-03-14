import time
from datetime import datetime
import asyncio
import os
from gc import get_objects
import dotenv
from dotenv import load_dotenv
from os import environ, execle, path
from itertools import count

from pyrogram import Client, enums, filters
from pyrogram.types import *
from Ubot import CMD_HELP, StartTime, app, ids
from Ubot.core.db import *
from pyrogram.raw.functions import Ping
from Ubot.modules.bot.inline import get_readable_time
from . import *

load_dotenv()

session_counter = count(1)

    
    
@Ubot("prem", cmds)
async def handle_grant_access(client: Client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.edit("Maaf, format yang Anda berikan salah. Mohon balas ke pengguna atau berikan username/user ID.")
            return
        username = text[1]
        user = await client.get_users(username)
        if user is None:
            await message.edit(f"`Maaf, pengguna {username} tidak ditemukan`.")
            return
        user_id = user.id

    if message.from_user.id not in ADMINS:
        await message.edit("`Maaf, hanya admin yang dapat memberikan akses.`")
        return

    if await grant_access(user_id):
        await message.edit(f"`Akses diberikan kepada pengguna {user_id}.`")
    else:
        await message.edit(f"`Pengguna {user_id} sudah memiliki akses sebelumnya.`")


@Ubot("unprem", cmds)
async def handle_revoke_access(client: Client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.edit("Maaf, format yang Anda berikan salah. Mohon balas ke pengguna atau berikan username/user ID.")
            return
        username = text[1]
        user = await client.get_users(username)
        if user is None:
            await message.edit(f"`Maaf, pengguna {username} tidak ditemukan.`")
            return
        user_id = user.id
    if message.from_user.id not in ADMINS:
        await message.edit("`Maaf, hanya admin yang dapat mencabut akses.`")
        return
    await delete_user_access(user_id)
    await message.edit(f"`Akses dicabut untuk pengguna {user_id}.`")
