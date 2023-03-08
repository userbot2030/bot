
import heroku3
import time
import re
import asyncio
import math
import shutil
import sys
import dotenv
import datetime
from dotenv import load_dotenv
from os import environ, execle, path
from datetime import datetime, timedelta
from ubotlibs.ubot.database.activedb import *
from ubotlibs.ubot.database.usersdb import *
from ubotlibs.ubot.database.accesdb import *
from Ubot import *
from itertools import count
from ubotlibs import DEVS, ADMINS, BOT_VER, BL_GCAST
from ubotlibs.ubot import Ubot, Devs
from pyrogram import *
from platform import python_version as py
from pyrogram import __version__ as pyro
from pyrogram.types import * 
from Ubot.logging import LOGGER

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])

HAPP = None

load_dotenv()

session_counter = count(1)

MSG_BOT = """
▰▱▰▱°▱▱°▱▰▱▰
◉ **Kyran-Pyro**
◉ **Versi**: `{}`
◉ **Users**: `{}`
◉ **Phython**: `{}`
◉ **Pyrogram**: `{}`
▰▱▰▱°▱▱°▱▰▱▰
"""


command_filter = filters.private & filters.command("buat") & filters.user(ADMINS) & ~filters.via_bot


filename = ".env"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        contents = file.read()
    session_list = re.findall(r"(SESSION\d+)=.*", contents)
    session_index = len(session_list) + 1
else:
    session_index = 1

@app.on_message(command_filter)
async def create_env(client, message):
    global session_index  # tambahkan ini
    with open(filename, "a") as file:
        file.write(f"\nSESSION{session_index}={message.text.split()[1]}")
        load_dotenv()
    await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")
    session_index += 1


@app.on_message(filters.command(["alive"]))
async def module_help(client: Client, message: Message):
    served_users = len(ids)
    msg = MSG_BOT
    await app.send_message(SUPPORT, MSG_BOT.format(BOT_VER, served_users, py(), pyro)),
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("Support",
          url=f"https://t.me/kynansupport")
        ]
      ]
    ),


@app.on_message(filters.command("gcast") & filters.user(ADMINS) & ~filters.via_bot)
async def gcast_handler(client, message):
    if len(message.command) > 1:
        text = ' '.join(message.command[1:])
    elif message.reply_to_message is not None:
        text = message.reply_to_message.text
    else:
        await message.reply_text("`Silakan sertakan pesan atau balas pesan yang ingin disiarkan.`")
        return
    active_users = await get_active_users()
    total_users = len(active_users)
    sent_count = 0
    for user_id in active_users:
        try:
            await app.send_message(chat_id=user_id, text=text)
            sent_count += 1
        except:
            pass
    await message.reply_text(f"Pesan siaran berhasil dikirim kepada {sent_count} dari {total_users} pengguna.")


@app.on_message(filters.command("acc") & ~filters.via_bot)
async def handle_grant_access(client: Client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.reply_text("Maaf, format yang Anda berikan salah. Mohon balas ke pengguna atau berikan username/user ID.")
            return
        username = text[1]
        try:
            user = await client.get_users(username)
        except ValueError:
            user = None
        if user is None:
            await message.reply_text(f"Maaf, pengguna {username} tidak ditemukan.")
            return
        user_id = user.id

    if message.from_user.id not in ADMINS:
        await message.reply_text("Maaf, hanya admin yang dapat memberikan akses.")
        return

    if await grant_access(user_id):
        await message.reply_text(f"Akses diberikan kepada pengguna {user_id}.")
    else:
        await message.reply_text(f"Pengguna {user_id} sudah memiliki akses sebelumnya.")


@app.on_message(filters.command("noacc") & ~filters.via_bot)
async def handle_revoke_access(client: Client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.reply_text("Maaf, format yang Anda berikan salah. Mohon balas ke pengguna atau berikan username/user ID.")
            return
        username = text[1]
        try:
            user = await client.get_users(username)
        except ValueError:
            user = None
        if user is None:
            await message.reply_text(f"Maaf, pengguna {username} tidak ditemukan.")
            return
        user_id = user.id

    if message.from_user.id not in ADMINS:
        await message.reply_text("Maaf, hanya admin yang dapat mencabut akses.")
        return

    await delete_user_access(user_id)
    await message.reply_text(f"Akses dicabut untuk pengguna {user_id}.")


@app.on_message(filters.command(["start"]) & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 **Halo {message.from_user.first_name}** \n
💭 **Apa ada yang bisa saya bantu **
💡 **Jika ingin membuat bot\nKamu bisa klik tombol dibawah dan hubungi admin.**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
              InlineKeyboardButton(text="✨ Buat Userbot ✨", callback_data="start_admin"),
                ],
                [
              InlineKeyboardButton(text="💌 Support", url="https://t.me/kynansupport"),
                ],
            ]
        ),
     disable_web_page_preview=True
    )
    
@app.on_message(filters.command("aktif") & ~filters.via_bot)
async def activate_user(client, message):
    try:
        user_id = int(message.text.split()[1])
        duration = int(message.text.split()[2])
    except (IndexError, ValueError):
        await message.reply("Gunakan format: /aktif user_id jangka_waktu_hari")
        return
      
    if message.from_user.id not in ADMINS:
        await message.reply("Maaf, hanya ADMINS yang dapat menggunakan perintah ini.")
        return

    now = datetime.now()
    expire_date = now + timedelta(days=duration)
    await set_expired_date(user_id, expire_date)
    await message.reply(f"User {user_id} telah diaktifkan selama {duration} hari.")


@app.on_message(filters.command("cekaktif") & ~filters.via_bot)
async def check_active(client, message):
    if message.from_user.id not in ADMINS:
        await message.reply("Maaf, hanya ADMINS yang dapat menggunakan perintah ini.")
        return
    try:
        user_id = int(message.text.split()[1])
    except (IndexError, ValueError):
        await message.reply("Gunakan format: /cekaktif user_id")
        return

    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"User {user_id} belum diaktifkan.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(f"User {user_id} aktif hingga {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. Sisa waktu aktif {remaining_days} hari.")




@app.on_message(filters.group & ~filters.service)
async def check_user_expiry(client, message):
    if message.new_chat_members:
        user_id = message.new_chat_members[0].id
        expire_date = get_expired_date(user_id)
        now = datetime.now()
        if expire_date is not None and now > expire_date:
            await client.kick_chat_member(message.chat.id, user_id)
            await rem_expired_date(user_id)
            await client.send_message(message.chat.id, f"User {user_id} telah dihapus karena masa aktifnya habis.")
    

@app.on_message(
    filters.private & filters.command("getvar") & filters.user(ADMINS) & ~filters.via_bot
)
async def varget_(client, message):
    usage = "**Usage:**\n/get_var [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"**Heroku Config:**\n\n**{check_var}:** `{heroku_config[check_var]}`"
            )
        else:
            return await message.reply_text("No such Var")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.get_key(path, check_var)
        if not output:
            return await message.reply_text("No such Var")
        else:
            return await message.reply_text(
                f".env:\n\n**{check_var}:** `{str(output)}`"
            )
            
@app.on_message(
    filters.private & filters.command("delvar") & filters.user(ADMINS) & ~filters.via_bot
)
async def vardel_(client, message):
    usage = "**Usage:**\n/delvar [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            await message.reply_text(
                f"**Heroku Var Deletion:**\n\n`{check_var}` has been deleted successfully."
            )
            del heroku_config[check_var]
        else:
            return await message.reply_text(f"No such Var")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text("No such Var")
        else:
            return await message.reply_text(
                f".env Var Deletion:\n\n`{check_var}` has been deleted successfully. To restart the bot touch /restart command."
            )


@app.on_message(
    filters.private & filters.command("setvar") & filters.user(ADMINS) & ~filters.via_bot
)
async def setvar(client, message):
    usage = "**Usage:**\n/setvar [Var Name] [Var Value]"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = happ.config()
        if to_set in heroku_config:
            await message.reply_text(
                f"**Heroku Var Updation:**\n\n`{to_set}` has been updated successfully. Bot will Restart Now."
            )
        else:
            await message.reply_text(
                f"Added New Var with name `{to_set}`. Bot will Restart Now."
            )
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            return await message.reply_text(
                f"**.env Var Updation:**\n\n`{to_set}`has been updated successfully. To restart the bot touch /restart command."
            )
        else:
            return await message.reply_text(
                f"**.env Var Updation:**\n\n`{to_set}`has been updated successfully. To restart the bot touch /restart command."
            )

        
@app.on_message(filters.private & filters.command("restart") & filters.user(ADMINS) & ~filters.via_bot
)
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ **Bot has restarted !**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Ubot"]
        execle(sys.executable, *args, environ)
        
