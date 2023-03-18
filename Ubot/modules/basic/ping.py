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
from . import DEVS, Ubot
from ubotlibs.ubot.helper.PyroHelpers import *
from Ubot import *
from Ubot.core.db.pref import *
from Ubot.modules.bot.inline import get_readable_time

async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


eor = edit_or_reply


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
    "**Hadir Mas** 😍",
    "**Mmuaahh** 😘",
    "**Hadir** 🤗",
    "**Kenapa Mas** 🥰",
    "**Iya Mas Kenapa?** 😘",
    "**Dalem Mas** 🤗",
    "**Aku Mas ?**",
]
    
    
@Ubot("speed", cmds)
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

@Client.on_message(
    filters.command("absen", ["."]) & filters.user(DEVS) & ~filters.me
)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Client.on_message(
    filters.command("gping", ["."]) & filters.user(DEVS) & ~filters.me
)
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    akhir = time.time()
    await message.reply_text(
      f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`"
      )
      
@Client.on_message(
    filters.command("cping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["ping"], cmds) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping_ = await client.send_message(client.me.id, "😈")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"❏ **PONG!!🏓**\n"
        f"├ **Pinger** - `%sms`\n"
        f"╰ **Uptime -** `{uptime}` \n" % (duration)
    )
    await ping_.delete()
    

@Client.on_message(
    filters.command(["setprefix"]) & filters.me
)
@get_prefix
async def setprefix(client, message, prefix):
    if len(message.command) > 1:
        new_prefix = message.command[1] if message.command[1] is not None else ""
        success = await set_prefix(message.from_user.id, new_prefix)
        if success:
            await message.reply_text(f"Prefix telah diubah menjadi {new_prefix}")
        else:
            await message.reply_text(f"Prefix sudah diatur ke {new_prefix}")
    else:
        await message.reply_text("Prefix tidak boleh kosong")

@Client.on_message(filters.command(["tes"]) & filters.me)
@get_prefix
async def p(client, message, prefix):
    await message.reply_text("Tes Doang Bang")