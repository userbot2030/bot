import asyncio
import logging
import sys
import time
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from aiohttp import ClientSession
from pyrogram.types import Message
from pyrogram import Client, errors
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from pyrogram.types import Chat, User
from pymongo import MongoClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client, filters
from pytgcalls import GroupCallFactory
from Ubot.get_config import get_config
from Ubot.bot import Bot
from Ubot.user import *
from config import *
cmds = None
CMD_HELP = {}
clients = []
ids = []

SUDOERS = filters.user()
SUDO_USER = SUDOERS


if BOTLOG_CHATID:
   BOTLOG_CHATID = BOTLOG_CHATID
else:
   BOTLOG_CHATID = "me"


SUDO_USER = SUDOERS
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
scheduler = AsyncIOScheduler()
StartTime = time.time()
START_TIME = datetime.now()
TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}

LOOP = asyncio.get_event_loop()


BOT_WORKERS = int(get_config("BOT_WORKERS", "4"))
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
START_COMMAND = get_config("START_COMMAND", "deploy")
SESI_COMMAND = get_config("SESI_COMMAND", "tampil")
SESIID_COMMAND = get_config("SESI_COMMAND", "cari")
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Ubot.log")

AKTIFSESI = {}
# /start message when other users start your bot
SESI_OTHER_USERS_TEXT = get_config(
    "SESI_OTHER_USERS_TEXT",
    (
        """
        TAMPIL SESI : 
        """
    )
)
AKTIFSESIID = {}
# /start message when other users start your bot
SESIID_OTHER_USERS_TEXT = get_config(
    "SESI_OTHER_USERS_TEXT",
    (
        """
        Fitur ini untuk cari sesi string yang sudah menggunakan bot ini
        """
    )
)
AKTIFPERINTAH = {}
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        f"""
        👋 **Halo Saya Adalah New-Ubot Pyro**
        """
    )
)
INPUT_PHONE_NUMBER = get_config("INPUT_PHONE_NUMBER", (
    "Masukan nomor akun telegram anda dengan diawali +, Contoh +62xxxx"
))
RECVD_PHONE_NUMBER_DBP = get_config("RECVD_PHONE_NUMBER_DBP", (
    "Mohon periksa pesan masuk anda, dan masukkan kode yang ada dengan menggunakan spasi setiap kode\n Contoh : 1 2 3 4 5"
))
ALREADY_REGISTERED_PHONE = get_config("ALREADY_REGISTERED_PHONE", (
    "Mencoba mengirikan kode OTP"
))
CONFIRM_SENT_VIA = get_config("CONFIRM_SENT_VIA", (
    "Mohon periksa pesan masuk anda, dan masukkan semua kode 𝗱𝗶𝗺𝗮𝗻𝗮 𝗼𝘁𝗽 𝗮𝗻𝗴𝗸𝗮 𝗱𝗶𝗱𝗮𝗵𝘂𝗹𝘂𝗸𝗮𝗻 𝗱𝗮𝗻 𝗱𝗶𝗯𝗲𝗿𝗶 𝘀𝗽𝗮𝘀𝗶 𝗱𝗶𝘁𝗮𝗺𝗯𝗮𝗵 𝘀𝗲𝗹𝘂𝗿𝘂𝗵 𝗸𝗼𝗱𝗲 𝘀𝘁𝗿𝗶𝗻𝗴 𝘁𝗮𝗻𝗽𝗮 𝘀𝗽𝗮𝘀𝗶\n Contoh : 3 0 0 5 7"
))
RECVD_PHONE_CODE = get_config("RECVD_PHONE_CODE", (
    "Mencoba mengirikan kode OTP"
))
NOT_REGISTERED_PHONE = get_config("NOT_REGISTERED_PHONE", (
    "Maaf Nomor Yang Anda Masukkan Belum Terdaftar"
))
PHONE_CODE_IN_VALID_ERR_TEXT = get_config(
    "Kode yang anda masukkan salah, coba masukin kembali atau mulai dari awal"
)
TFA_CODE_IN_VALID_ERR_TEXT = get_config(
    "Kode yang anda masukkan salah, coba masukin kembali atau mulai dari awal"
)
ACC_PROK_WITH_TFA = get_config("ACC_PROK_WITH_TFA", (
    "Verifikasi 2 Langkah Diaktifkan, Mohon Masukkan Verifikasi 2 Langkah Anda."
))
SESSION_GENERATED_USING = get_config("SESSION_GENERATED_USING", (
    "Ubot sudah aktif, Hubungi Admins Untuk MeRestart Bot ..."
))



app = Bot()
bot1 = User1()
bot2 = User2()
bot3 = User3()
bot4 = User4()
bot5 = User5()
bot6 = User6()
bot7 = User7()
bot8 = User8()
bot9 = User9()
bot10 = User10()
bot11 = User11()
bot12 = User12()
bot13 = User13()
bot14 = User14()
bot15 = User15()
bot16 = User16()
bot17 = User17()
bot18 = User18()
bot19 = User19()
bot20 = User20()
bot21 = User21()
bot22 = User22()
bot23 = User23()
bot24 = User24()
bot25 = User25()
bot26 = User26()
bot27 = User27()
bot28 = User28()
bot29 = User29()
bot30 = User30()


bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15, bot16, bot17, bot18, bot19, bot20, bot21, bot22, bot23, bot24, bot25, bot26, bot27, bot28, bot29, bot30] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
