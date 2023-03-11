import asyncio
import logging
import sys
import time
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client, filters
from pytgcalls import GroupCallFactory
from Ubot.get_config import get_config
from config import *
cmds = ["!", "?", "*", "-", "^", "."]
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
START_COMMAND = get_config("START_COMMAND", "buat_userbot")
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Ubot.log")

AKTIFPERINTAH = {}
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        f"""
        👋 **Halo Saya Adalah Ubot-Pyro**
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
    "Mohon periksa pesan masuk anda, dan masukkan kode yang ada dengan menggunakan spasi setiap kode\n Contoh : 1 2 3 4 5i {}"
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
    "client sudah aktif, Hubungi Admins Untuk MeRestart client ..."
))

if not BOT_TOKEN:
   LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
   sys.exit()


app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Ubot/modules/bot"),
    in_memory=True,
)

client1 = (
    Client(
        name="client1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION1,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION1:
        clients.append(client1)

client2 = (
    Client(
        name="client2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION2,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION2:
    clients.append(client2)

client3 = (
    Client(
        name="client3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION3,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION3:
    clients.append(client3)

client4 = (
    Client(
        name="client4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION4,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION4:
    clients.append(client4)

client5 = (
    Client(
        name="client5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION5,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION5:
    clients.append(client5)
    
client6 = (
    Client(
        name="client6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION6,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION6:
    clients.append(client6)

client7 = (
    Client(
        name="client7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION7,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION7:
    clients.append(client7)

client8 = (
    Client(
        name="client8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION8,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION8:
    clients.append(client8)

client9 = (
    Client(
        name="client9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION9,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION9:
    clients.append(client9)

client10 = (
    Client(
        name="client10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION10,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION10:
        clients.append(client10)

client11 = (
    Client(
        name="client11",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION11,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION11:
    clients.append(client11)
client12 = (
    Client(
        name="client12",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION12,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION12:
     clients.append(client12)

client13 = (
    Client(
        name="client13",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION13,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION13:
     clients.append(client13)

client14 = (
    Client(
        name="client14",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION14,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION14:
     clients.append(client14)
     
client15 = (
    Client(
        name="client15",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION15,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION15:
     clients.append(client15)

client16 = (
    Client(
        name="client16",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION16,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION16:
     clients.append(client16)

client17 = (
    Client(
        name="client17",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION17,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION17:
     clients.append(client17)

client18 = (
    Client(
        name="client18",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION18,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION18:
    clients.append(client18)

client19 = (
    Client(
        name="client19",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION19,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION19:
    clients.append(client19)

client20 = (
    Client(
        name="client20",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION20,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION20:
    clients.append(client20)

client21 = (
    Client(
        name="client21",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION21,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION21:
    clients.append(client21)

client22 = (
    Client(
        name="client22",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION22,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION22:
     clients.append(client22)

client23 = (
    Client(
        name="client23",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION23,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION23:
     clients.append(client23)

client24 = (
    Client(
        name="client24",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION24,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION24:
     clients.append(client24)

client25 = (
    Client(
        name="client25",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION25,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION25:
     clients.append(client25)

client26 = (
    Client(
        name="client26",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION26,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION26:
    clients.append(client26)

client27 = (
    Client(
        name="client27",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION27,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION27:
     clients.append(client27)

client28 = (
    Client(
        name="client28",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION28,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION28:
     clients.append(client28)

client29 = (
    Client(
        name="client29",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION29,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION29:
     clients.append(client29)

client30 = (
    Client(
        name="client30",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION30,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION30:
     clients.append(client30)

client31 = (
    Client(
        name="client31",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION31,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION31:
     clients.append(client31)

client32 = (
    Client(
        name="client32",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION32,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION32:
     clients.append(client32)

client33 = (
    Client(
        name="client33",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION33,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION33:
     clients.append(client33)

client34 = (
    Client(
        name="client34",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION34,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION34:
     clients.append(client34)

client35 = (
    Client(
        name="client35",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION35,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION35:
     clients.append(client35)

client36 = (
    Client(
        name="client36",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION36,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION36:
     clients.append(client36)

client37 = (
    Client(
        name="client37",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION37,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION37:
     clients.append(client37)

client38 = (
    Client(
        name="client38",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION38,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION38:
     clients.append(client38)

client39 = (
    Client(
        name="client39",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION39,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION39:
     clients.append(client39)

client40 = (
    Client(
        name="client40",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION40,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION40:
     clients.append(client40)

client41 = (
    Client(
        name="client41",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION41,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION41:
     clients.append(client41)

client42 = (
    Client(
        name="client42",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION42,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION42:
     clients.append(client42)

client43 = (
    Client(
        name="client43",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION43,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION43:
     clients.append(client43)

client44 = (
    Client(
        name="client44",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION44,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION44:
     clients.append(client44)

client45 = (
    Client(
        name="client45",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION45,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION45:
     clients.append(client45)

client46 = (
    Client(
        name="client46",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION46,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION46:
     clients.append(client46)

client47 = (
    Client(
        name="client47",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION47,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION47:
     clients.append(client47)

client48 = (
    Client(
        name="client48",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION48,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION48:
     clients.append(client48)

client49 = (
    Client(
        name="client49",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION49,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION49:
     clients.append(client49)

client50 = (
    Client(
        name="client50",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION50,
        plugins=dict(root="Ubot/modules"),
    )
)
if SESSION50:
     clients.append(client50)

client51 = (
    Client(
        name="client51",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION51,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION51
    else None
)

client52 = (
    Client(
        name="client52",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION52,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION52
    else None
)

client53 = (
    Client(
        name="client53",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION53,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION53
    else None
)

client54 = (
    Client(
        name="client54",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION54,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION54
    else None
)

client55 = (
    Client(
        name="client55",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION55,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION55
    else None
)
client56 = (
    Client(
        name="client56",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION56,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION56
    else None
)
client57 = (
    Client(
        name="client57",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION57,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION57
    else None
)
client58 = (
    Client(
        name="client58",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION58,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION58
    else None
)
client59 = (
    Client(
        name="client59",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION59,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION59
    else None
)
client60 = (
    Client(
        name="client60",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION60,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION60
    else None
)

client61 = (
    Client(
        name="client61",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION61,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION61
    else None
)

client62 = (
    Client(
        name="client62",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION62,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION62
    else None
)

client63 = (
    Client(
        name="client63",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION63,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION63
    else None
)

client64 = (
    Client(
        name="client64",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION64,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION64
    else None
)

client65 = (
    Client(
        name="client65",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION65,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION65
    else None
)
client66 = (
    Client(
        name="client66",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION66,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION66
    else None
)
client67 = (
    Client(
        name="client67",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION67,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION67
    else None
)
client68 = (
    Client(
        name="client68",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION68,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION68
    else None
)
client69 = (
    Client(
        name="client69",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION69,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION69
    else None
)
client70 = (
    Client(
        name="client70",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION70,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION70
    else None
)

client71 = (
    Client(
        name="client71",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION71,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION71
    else None
)

client72 = (
    Client(
        name="client72",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION72,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION72
    else None
)

client73 = (
    Client(
        name="client73",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION73,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION73
    else None
)

client74 = (
    Client(
        name="client74",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION74,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION74
    else None
)

client75 = (
    Client(
        name="client75",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION75,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION75
    else None
)
client76 = (
    Client(
        name="client76",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION76,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION76
    else None
)
client77 = (
    Client(
        name="client77",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION77,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION77
    else None
)
client78 = (
    Client(
        name="client78",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION78,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION78
    else None
)
client79 = (
    Client(
        name="client79",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION79,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION79
    else None
)
client80 = (
    Client(
        name="client80",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION80,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION80
    else None
)

client81 = (
    Client(
        name="client81",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION81,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION81
    else None
)

client82 = (
    Client(
        name="client82",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION82,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION82
    else None
)

client83 = (
    Client(
        name="client83",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION83,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION83
    else None
)

client84 = (
    Client(
        name="client84",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION84,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION84
    else None
)

client85 = (
    Client(
        name="client85",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION85,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION85
    else None
)
client86 = (
    Client(
        name="client86",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION86,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION86
    else None
)
client87 = (
    Client(
        name="client87",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION87,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION87
    else None
)
client88 = (
    Client(
        name="client88",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION88,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION88
    else None
)
client89 = (
    Client(
        name="client89",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION89,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION89
    else None
)
client90 = (
    Client(
        name="client90",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION90,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION90
    else None
)

client91 = (
    Client(
        name="client91",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION91,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION91
    else None
)

client92 = (
    Client(
        name="client92",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION92,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION92
    else None
)

client93 = (
    Client(
        name="client93",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION93,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION93
    else None
)

client94 = (
    Client(
        name="client94",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION94,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION94
    else None
)

client95 = (
    Client(
        name="client95",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION95,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION95
    else None
)
client96 = (
    Client(
        name="client96",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION96,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION96
    else None
)
client97 = (
    Client(
        name="client97",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION97,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION97
    else None
)
client98 = (
    Client(
        name="client98",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION98,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION98
    else None
)
client99 = (
    Client(
        name="client99",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION99,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION99
    else None
)
client100 = (
    Client(
        name="client100",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION100,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION100
    else None
)
client101 = (
    Client(
        name="client101",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION101,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION101
    else None
)

client102 = (
    Client(
        name="client102",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION102,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION102
    else None
)

client103 = (
    Client(
        name="client103",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION103,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION103
    else None
)

client104 = (
    Client(
        name="client104",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION104,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION104
    else None
)

client105 = (
    Client(
        name="client105",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION105,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION105
    else None
)
client106 = (
    Client(
        name="client106",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION106,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION106
    else None
)
client107 = (
    Client(
        name="client107",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION107,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION107
    else None
)
client108 = (
    Client(
        name="client108",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION108,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION108
    else None
)
client109 = (
    Client(
        name="client109",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION109,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION109
    else None
)
client110 = (
    Client(
        name="client110",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION110,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION110
    else None
)
client111 = (
    Client(
        name="client111",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION111,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION111
    else None
)

client112 = (
    Client(
        name="client112",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION112,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION112
    else None
)

client113 = (
    Client(
        name="client113",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION113,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION113
    else None
)

client114 = (
    Client(
        name="client114",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION114,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION114
    else None
)

client115 = (
    Client(
        name="client115",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION115,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION115
    else None
)
client116 = (
    Client(
        name="client116",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION116,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION116
    else None
)
client117 = (
    Client(
        name="client117",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION117,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION117
    else None
)
client118 = (
    Client(
        name="client118",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION118,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION118
    else None
)
client119 = (
    Client(
        name="client119",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION119,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION119
    else None
)
client120 = (
    Client(
        name="client120",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION120,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION120
    else None
)
client121 = (
    Client(
        name="client121",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION121,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION121
    else None
)

client122 = (
    Client(
        name="client122",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION122,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION122
    else None
)

client123 = (
    Client(
        name="client123",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION123,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION123
    else None
)

client124 = (
    Client(
        name="client124",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION124,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION124
    else None
)

client125 = (
    Client(
        name="client125",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION125,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION125
    else None
)
client126 = (
    Client(
        name="client126",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION126,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION126
    else None
)
client127 = (
    Client(
        name="client127",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION127,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION127
    else None
)
client128 = (
    Client(
        name="client128",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION128,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION128
    else None
)
client129 = (
    Client(
        name="client129",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION129,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION129
    else None
)
client130 = (
    Client(
        name="client130",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION130,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION130
    else None
)
client131 = (
    Client(
        name="client131",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION131,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION131
    else None
)

client132 = (
    Client(
        name="client132",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION132,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION132
    else None
)

client133 = (
    Client(
        name="client133",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION133,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION133
    else None
)

client134 = (
    Client(
        name="client134",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION134,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION134
    else None
)

client135 = (
    Client(
        name="client135",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION135,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION135
    else None
)
client136 = (
    Client(
        name="client136",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION136,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION136
    else None
)
client137 = (
    Client(
        name="client137",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION137,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION137
    else None
)
client138 = (
    Client(
        name="client138",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION138,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION138
    else None
)
client139 = (
    Client(
        name="client139",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION139,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION139
    else None
)
client140 = (
    Client(
        name="client140",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION140,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION140
    else None
)
client141 = (
    Client(
        name="client141",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION141,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION141
    else None
)

client142 = (
    Client(
        name="client142",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION142,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION142
    else None
)

client143 = (
    Client(
        name="client143",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION143,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION143
    else None
)

client144 = (
    Client(
        name="client144",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION144,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION144
    else None
)

client145 = (
    Client(
        name="client145",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION145,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION145
    else None
)
client146 = (
    Client(
        name="client146",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION146,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION146
    else None
)
client147 = (
    Client(
        name="client147",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION147,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION147
    else None
)
client148 = (
    Client(
        name="client148",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION148,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION148
    else None
)
client149 = (
    Client(
        name="client149",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION149,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION149
    else None
)
client150 = (
    Client(
        name="client150",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION150,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION150
    else None
)
client151 = (
    Client(
        name="client151",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION151,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION151
    else None
)

client152 = (
    Client(
        name="client152",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION152,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION152
    else None
)

client153 = (
    Client(
        name="client153",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION153,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION153
    else None
)

client154 = (
    Client(
        name="client154",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION154,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION154
    else None
)

client155 = (
    Client(
        name="client155",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION155,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION155
    else None
)
client156 = (
    Client(
        name="client156",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION156,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION156
    else None
)
client157 = (
    Client(
        name="client157",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION157,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION157
    else None
)
client158 = (
    Client(
        name="client158",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION158,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION158
    else None
)
client159 = (
    Client(
        name="client159",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION159,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION159
    else None
)
client160 = (
    Client(
        name="client160",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION160,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION160
    else None
)

client161 = (
    Client(
        name="client161",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION161,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION161
    else None
)

client162 = (
    Client(
        name="client162",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION162,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION162
    else None
)

client163 = (
    Client(
        name="client163",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION163,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION163
    else None
)

client164 = (
    Client(
        name="client164",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION164,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION164
    else None
)

client165 = (
    Client(
        name="client165",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION165,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION165
    else None
)
client166 = (
    Client(
        name="client166",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION166,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION166
    else None
)
client167 = (
    Client(
        name="client167",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION167,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION167
    else None
)
client168 = (
    Client(
        name="client168",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION168,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION168
    else None
)
client169 = (
    Client(
        name="client169",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION169,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION169
    else None
)
client170 = (
    Client(
        name="client170",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION170,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION170
    else None
)

client171 = (
    Client(
        name="client171",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION171,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION171
    else None
)

client172 = (
    Client(
        name="client172",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION172,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION172
    else None
)

client173 = (
    Client(
        name="client173",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION173,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION173
    else None
)

client174 = (
    Client(
        name="client174",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION174,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION174
    else None
)

client175 = (
    Client(
        name="client175",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION175,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION175
    else None
)
client176 = (
    Client(
        name="client176",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION176,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION176
    else None
)
client177 = (
    Client(
        name="client177",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION177,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION177
    else None
)
client178 = (
    Client(
        name="client178",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION178,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION178
    else None
)
client179 = (
    Client(
        name="client179",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION179,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION179
    else None
)
client180 = (
    Client(
        name="client180",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION180,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION180
    else None
)

client181 = (
    Client(
        name="client181",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION181,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION181
    else None
)

client182 = (
    Client(
        name="client182",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION182,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION182
    else None
)

client183 = (
    Client(
        name="client183",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION183,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION183
    else None
)

client184 = (
    Client(
        name="client184",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION184,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION184
    else None
)

client185 = (
    Client(
        name="client185",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION185,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION185
    else None
)
client186 = (
    Client(
        name="client186",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION186,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION186
    else None
)
client187 = (
    Client(
        name="client187",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION187,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION187
    else None
)
client188 = (
    Client(
        name="client188",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION188,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION188
    else None
)
client189 = (
    Client(
        name="client189",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION189,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION189
    else None
)
client190 = (
    Client(
        name="client190",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION190,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION190
    else None
)

client191 = (
    Client(
        name="client191",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION191,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION191
    else None
)

client192 = (
    Client(
        name="client192",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION192,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION192
    else None
)

client193 = (
    Client(
        name="client193",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION193,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION193
    else None
)

client194 = (
    Client(
        name="client194",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION194,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION194
    else None
)

client195 = (
    Client(
        name="client195",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION195,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION195
    else None
)
client196 = (
    Client(
        name="client196",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION196,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION196
    else None
)
client197 = (
    Client(
        name="client197",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION197,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION197
    else None
)
client198 = (
    Client(
        name="client198",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION198,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION198
    else None
)
client199 = (
    Client(
        name="client199",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION199,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION199
    else None
)
client200 = (
    Client(
        name="client200",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION200,
        plugins=dict(root="Ubot/modules"),
    )
    if SESSION200
    else None
)



clients = [client for client in [client1, client2, client3, client4, client5, client6, client7, client8, client9, client10, client11, client12, client13, client14, client15, client16, client17, client18, client19, client20, client21, client22, client23, client24, client25, client26, client27, client28, client29, client30, client31, client32, client33, client34, client35, client36, client37, client38, client39, client40, client41, client42, client43, client44, client45, client46, client47, client48, client49, client50, client51, client52, client53, client54, client55, client56, client57, client58, client59, client60, client61, client62, client63, client64, client65, client66, client67, client68, client69, client70, client71, client72, client73, client74, client75, client76, client77, client78, client79, client80, client81, client82, client83, client84, client85, client86, client87, client88, client89, client90, client91, client92, client93, client94, client95, client96, client97, client98, client99, client100, client101, client102, client103, client104, client105, client106, client107, client108, client109, client110, client111, client112, client113, client114, client115, client116, client117, client118, client119, client120, client121, client122, client123, client124, client125, client126, client127, client128, client129, client130, client131, client132, client133, client134, client135, client136, client137, client138, client139, client140, client141, client142, client143, client144, client145, client146, client147, client148, client149, client150, client151, client152, client153, client154, client155, client156, client157, client158, client159, client160, client161, client162, client163, client164, client165, client166, client167, client168, client169, client170, client171, client172, client173, client174, client175, client176, client177, client178, client179, client180, client181, client182, client183, client184, client185, client186, client187, client188, client89, client190, client191, client192, client193, client194, client195, client196, client197, client198, client199, client200] if client]

for client in clients:
    if not hasattr(client, "group_call"):
        setattr(client, "group_call", GroupCallFactory(client).get_group_call())