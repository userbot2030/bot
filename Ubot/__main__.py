import importlib
import time
from datetime import datetime
import asyncio
from pyrogram import idle
from pyrogram.errors import RPCError
from uvloop import install
from ubotlibs import *
from Ubot import BOTLOG_CHATID, aiosession, bot1, bots, app, ids, LOOP
from platform import python_version as py
from Ubot.logging import LOGGER
from pyrogram import __version__ as pyro

from Ubot.modules import ALL_MODULES
from Ubot.core.db import *
from config import SUPPORT, CHANNEL, CMD_HNDLR, ADMIN1_ID, ADMIN2_ID, ADMIN3_ID, ADMIN4_ID, ADMIN5_ID, ADMIN6_ID, ADMIN7_ID
import os
from dotenv import load_dotenv


MSG_BOT = """
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**New Ubot Actived ✅**
◉ **Phython**: `{}`
◉ **Pyrogram**: `{}`
◉ **Users**: `{}`
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

MSG_ON = """
**New Ubot Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
◉ **Masa Aktif** : `{}`
◉ **Akan Berakhir**: `{}`
**Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

MSG = """
**Users**: `{}`
**ID**: `{}`
"""


async def main():
    await app.start()
    LOGGER("Ubot").info("Memulai Ubot Pyro..")
    LOGGER("Ubot").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            LOGGER("Ubot").info("Startup Completed")
            LOGGER("√").info(f"Started as {ex.first_name} | {ex.id} ")
            await add_user(ex.id)
            user_active_time = await get_active_time(ex.id)
            active_time_str = str(user_active_time.days) + " Hari"
            expired_date = await get_expired_date(ex.id)
            remaining_days = (expired_date - datetime.now()).days
            msg = f"{ex.first_name} ({ex.id}) - Masa Aktif: {active_time_str}"
            ids.append(ex.id)
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, pyro, py(), active_time_str, remaining_days, CMD_HNDLR))
            user = len(ids)
        except Exception as e:
            LOGGER("X").info(f"{e}")
            if "Telegram says:" in str(e):
                load_dotenv()
                session_name = None
                for i in range(1, 201):
                    if os.getenv(f"SESSION{i}") == str(e):
                        session_name = f"SESSION{i}"
                        os.environ.pop(session_name)
                        LOGGER("Ubot").info(f"Removed {session_name} from .env file due to error.")
                        await app.send_message(SUPPORT, f"Removed {session_name} from .env file due to error.")
                        break
                if session_name is None:
                   LOGGER("Ubot").info(f"Could not find session name in .env file for error: {str(e)}")
    await app.send_message(SUPPORT, MSG_BOT.format(py(), pyro, user))
    await idle()
    await aiosession.close()
    for ex_id in ids:
        await remove_user(ex_id)


              

if __name__ == "__main__":
    LOGGER("Ubot").info("Starting  Ubot")
    install()
    LOOP.run_until_complete(main())