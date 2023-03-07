# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
import random
import time
import traceback
from sys import version as pyver
from datetime import datetime
import asyncio
import os
from gc import get_objects

from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from Ubotlibs.Ubot.helper.data import Data
from Ubotlibs.Ubot.helper.inline import inline_wrapper, paginate_help
from Ubotlibs import BOT_VER
from Ubotlibs.Ubot.database.activedb import *
from pyrogram.raw.functions import Ping
from Ubotlibs.Ubot import Ubot, Devs
from Ubot import CMD_HELP, StartTime, app, ids, cmds, app
from config import ADMIN1_ID, ADMIN2_ID, ADMIN3_ID, ADMIN4_ID, ADMIN5_ID

OWNER_ID = 951454060
SUDO_ID = [902478883, 2067434944, 1947740506]

def support():
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/kynansupport"),
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/kontenfilm"),
        ],
    ]
    return buttons

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    
    
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

@app.on_inline_query(filters.regex("user_alive_command"))
async def _(client, inline_query):
    get_id = inline_query.query.split()[1]
    m = [obj for obj in get_objects() if id(obj) == int(get_id)][0]
    users = 0
    group = 0
    async for dialog in m._client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            group += 1
    if m._client.me.id == OWNER:
        status = "OWNER"
    elif m._client.me.id in SUDO_ID:
        status = "ADMIN"
    else:
        status = "MEMBER"
    start = datetime.now()
    await m._client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    msg = f"""
<b>{app.me.first_name.split()[0]}</b>
   <b>status:</b> <code>[{status}]</code>
      <b>dc_id:</b> <code>{my.me.dc_id}
      <b>ping_dc:</b> <code>{ping} ms</code>
      <b>peer_users:</b> <code>{users} users</code>
      <b>peer_group:</b> <code>{group} group</code>
      <b>{app.me.first_name.split()[0]}_uptime:</b> <code>{uptime}</code>
"""
    await client.answer_inline_query(
        inline_query.id,
        cache_time=300,
        results=[
            (
                InlineQueryResultArticle(
                    title="tomi",
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )

@app.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


async def alive_function(client: Client, message: Message, answers, query):
    uptime = await get_readable_time((time.time() - StartTime))
    ex = await client.get_me()
    user = len( await get_active_users())
    user_active_time = await get_active_time(ex.id)
    active_time_str = str(user_active_time.days) + " Hari " + str(user_active_time.seconds // 3600) + " Jam"
    buttons = support()
    users = 0
    group = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
          users += 1
        elif dialog.chat.type in (enums.ChatType.GROUP,
        enums.ChatType.SUPERGROUP):
          group += 1
    if client.me.id == OWNER_ID:
      status = "**OWNER**"
    elif client.me.id in SUDO_ID:
      status = "**ADMIN**"
    else:
      status = "**MEMBER**"
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    answer_text = (
      f"**Kyran-Pyro**\n"
      f"     <b>◉ Status : [{status}]</b>\n"
      f"     <b>◉ Master :</b> {client.me.mention} \n"
      f"     <b>◉ Users :</b> <code>{user}</code>\n"
      f"     <b>◉ Plugins :</b> <code>{len(CMD_HELP)}</code> \n"
      f"     <b>◉ Ping DC:</b> <code>{ping} ms</code>\n"
      f"     <b>◉ Users Count :</b> <code>{users} users</code>\n"
      f"     <b>◉ Groups Count :</b> <code>{group} group</code>\n"
      f"     <b>◉ Uptime :</b> <code>{uptime}</code>\n"
      f"     <b>◉ Aktif :</b> <code>{active_time_str}</code>\n"
      )
    answers.append(
        InlineQueryResultArticle(
            title="kynan",
            description="Check Bot's Stats",
            thumb_url="https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
            input_message_content=InputTextMessageContent(
                answer_text, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ʜᴇʟᴘ", callback_data="helper")]]
            ),
        )
    )
    return answers

async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers


@app.on_inline_query()
# @inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        if text.strip() == "":
            return
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
        elif string_given.startswith("kynan"):
            answers = await alive_function(client, message, answers, query)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
      