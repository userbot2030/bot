# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import time
import random
import speedtest
import asyncio
import re
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from datetime import datetime
from ubotlibs import *
from ubotlibs.ubot.helper import edit_or_reply
from ubotlibs.ubot.database.accesdb import *
from Ubot import *
from Ubot.modules.bot.inline import get_readable_time

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n"
        "Ping ➠ `{ping}` ms\n"
        "Download ➠ `{download}`\n"
        "Upload ➠ `{upload}`\n"
        "ISP ➠ __{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"
    
kopi = [
    "**Hadir Sayang** 😍",
    "**Mmuaahh** 😘",
    "**Hadir Cinta** 🤗",
    "**Kenapa ganteng** 🥰",
    "**Iya sayang Kenapa?** 😘",
    "**Dalem sayang** 🤗",
]

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "Harus banget gua jawab?",
                 "Apaansi nanya mulu lu",
                 "Emang bener?",
                 "Mana gua tau ",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Nanya Mulu lu"
                 ]
                 
KENAPA_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "Harus banget gua jawab?",
                 "Apaansi nanya mulu lu",
                 "Emang bener?",
                 "Mana gua tau ",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Nanya Mulu lu"
                 "Karna Kamu Jamet"
                 ]
                 
BAGAIMANA_STRING = ["Tau ya", 
                 "Ngapa si ?", 
                 "Jamet", 
                 "Diem Jamet", 
                 "Berisik lu", 
                 "Bacot",
                 "Astaghfirullah, Anj",
                 "Kan Udah Dibilang Jangan Budeg",
                 "Apaansi nanya mulu lu",
                 "Emang bener?",
                 "Mana gua tau ",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Karna Kamu Jamet"
                 ]
    
    
@Ubot("speed", cmds)
@check_access
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )

@Client.on_message(filters.command("absen", ".") & filters.user(DEVS) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Devs("gping")
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    akhir = time.time()
    await message.reply_text(
      f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`"
      )
      
@Devs("cping")
@Ubot("ping", cmds)
@check_access
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping_ = await client.send_message(client.me.id, "😈")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"⛶ **PONG!!🏓**\n"
        f"├╼ **Pinger** - `%sms`\n"
        f"╰╼ **Uptime -** `{uptime}` \n" % (duration)
    )
    await ping_.delete()