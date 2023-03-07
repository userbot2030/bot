# Credits Thx Tomi Setiawan

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
from Ubot import CMD_HELP, StartTime, app, ids, cmds
from ubotlibs.ubot.database.activedb import *
from ubotlibs.ubot.database.usersdb import *
from ubotlibs.ubot.database.accesdb import *
from pyrogram.raw.functions import Ping
from Ubot.modules.bot.inline import get_readable_time
from ubotlibs import *


OWNER_ID = 951454060
SUDO_ID = [1970636001, 902478883, 2099942562, 2067434944, 1947740506, 1897354060, 1694909518]

load_dotenv()

session_counter = count(1)


def support():
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/kynansupport"),
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/kontenfilm"),
        ],
    ]
    return buttons
    
@Client.on_message(filters.command("login", cmds) & filters.user(ADMINS) & filters.me)
@check_access
async def create_env(client, message):
    try:
        session = message.text.split()[1]
    except IndexError:
        await message.reply_text("Format yang benar adalah: login <session>")
        return

    filename = ".env"
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            contents = file.read()
            if session in contents:
                await message.reply_text(f"Session sudah tersimpan pada {filename}.")
                return
            else:
                session_index = next(session_counter)
                with open(filename, "a") as file:
                    file.write(f"\nSESSION{session_index}={session}")
                    load_dotenv()
                await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")
    else:
        session_index = next(session_counter)
        with open(filename, "w") as file:
            file.write(f"SESSION{session_index}={session}")
            load_dotenv()
        await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")

    
@Ubot("acc", cmds)
@check_access
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


@Ubot("noacc", cmds)
@check_access
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


@Ubot(["alive"], cmds)
@check_access
async def alive(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    ex = await client.get_me()
    user = len( await get_active_users())
    user_active_time = await get_active_time(ex.id)
    active_time_str = str(user_active_time.days) + " Hari " + str(user_active_time.seconds // 3600) + " Jam"
    buttons = support()
    users = 0
    group = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            group += 1
    if client.me.id == OWNER_ID:
        status = "**OWNER**"
    elif client.me.id in SUDO_ID:
        status = "**ADMIN**"
    else:
        status = "**MEMBER**"
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    await message.reply(
        f"**Ubot-Pyro**\n"
        f"     <b>◉ Status : [{status}]</b>\n"
        f"     <b>◉ Master :</b> {client.me.mention} \n"
        f"     <b>◉ Users :</b> <code>{user}</code>\n"
        f"     <b>◉ Plugins :</b> <code>{len(CMD_HELP)} Modules</code> \n"
        f"     <b>◉ Ping DC:</b> <code>{ping} ms</code>\n"
        f"     <b>◉ Users Count :</b> <code>{users} users</code>\n"
        f"     <b>◉ Groups Count :</b> <code>{group} group</code>\n"
        f"     <b>◉ Uptime :</b> <code>{uptime}</code>\n"
        f"     <b>◉ Aktif :</b> <code>{active_time_str}</code>\n",
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )