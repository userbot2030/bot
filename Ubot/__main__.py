import importlib
import time
from datetime import datetime
import asyncio
from asyncio import get_event_loop_policy
from pyrogram import idle
from uvloop import install
from ubotlibs import *
from Ubot import BOTLOG_CHATID, aiosession, bot1, bots, app, ids, LOOP
from platform import python_version as py
from Ubot.logging import LOGGER
from pyrogram import __version__ as pyro
from pyrogram import *
from pyrogram.types import *
from Ubot.modules import ALL_MODULES
from ubotlibs.ubot.database.activedb import *
from ubotlibs.ubot.database.usersdb import *
from config import SUPPORT, CHANNEL, CMD_HNDLR, ADMIN1_ID, ADMIN2_ID, ADMIN3_ID, ADMIN4_ID, ADMIN5_ID, ADMIN6_ID
import os
from dotenv import load_dotenv


MSG_BOT = """
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Alive
◉ **Phython**: `{}`
◉ **Pyrogram**: `{}`
◉ **Users**: `{}`
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

MSG_ON = """
**Kyran-Pyro Actived ✅**
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


@app.on_callback_query(filters.regex("start_admin"))
async def start_admin(_, query: CallbackQuery):
    ADMIN1 = ADMIN1_ID[0]
    ADMIN2 = ADMIN2_ID[0]
    ADMIN3 = ADMIN3_ID[0]
    ADMIN4 = ADMIN4_ID[0]
    ADMIN5 = ADMIN5_ID[0]
    return await query.edit_message_text(
        f"""<b> ☺️** Silakan hubungi admin dibawah ini untuk membuat userbot**</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="👮‍♂ Admin 1", user_id=ADMIN1),
                    InlineKeyboardButton(text="👮‍♂ Admin 2", user_id=ADMIN2),
                ],
                [
                    InlineKeyboardButton("👮‍♂ Admin 3", user_id=ADMIN3),
                    InlineKeyboardButton(text="👮‍♂ Admin 4", user_id=ADMIN4),
                  ],
                  [
                    InlineKeyboardButton(text="👮‍♂ Admin 5", user_id=ADMIN5),
                    
                  ],
                  [
                     InlineKeyboardButton(text="Tutup", callback_data="close"),
                  ],
             ]
        ),
    )


@app.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

async def main():
    await app.run()
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
            active_time_str = str(user_active_time.days) + " Hari " + str(user_active_time.seconds // 3600) + " Jam"
            expired_date = await get_expired_date(ex.id)
            remaining_days = (expired_date - datetime.now()).days
            msg = f"{ex.first_name} ({ex.id}) - Masa Aktif: {active_time_str}"
            ids.append(ex.id)
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, pyro, py(), active_time_str, remaining_days, CMD_HNDLR))
            user = len( await get_active_users())
        except Exception as e:
            LOGGER("X").info(f"{e}")
            if "Telegram says" in str(e):
                load_dotenv()
                for i in range(1, 201):
                    if os.getenv(f"SESSION{i}") == str(e):
                        os.environ.pop(f"SESSION{i}")
                        LOGGER("Ubot").info(f"Removed SESSION{i} from .env file due to error.")
                        await app.send_message(SUPPORT, f"Removed SESSION{i} from .env file due to error.")
                        break
    await app.send_message(SUPPORT, MSG_BOT.format(py(), pyro, user))
    await idle()
    for ex_id in ids:
        await remove_user(ex_id)


              
if __name__ == "__main__":
   install()
   LOOP.run_until_complete(main())
   LOGGER("Info").info("Stop Ubot Pyro")