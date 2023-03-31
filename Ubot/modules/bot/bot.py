
import traceback
import re
from pyrogram import Client, filters
from pyrogram.errors import MessageDeleteForbidden
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Ubot import CMD_HELP, app
from Ubot.core.data import Data
from Ubot.core.inline import cb_wrapper, paginate_help
from Ubot import ids as users
from config import SUPPORT, CHANNEL, CMD_HNDLR, ADMIN1_ID, ADMIN2_ID, ADMIN3_ID, ADMIN4_ID, ADMIN5_ID, ADMIN6_ID, ADMIN7_ID


@Client.on_callback_query()
async def _callbacks(_, callback_query: CallbackQuery):
    query = callback_query.data.lower()
    bot_me = await app.get_me()
    text = "**Menu Bantuan**"
    if query == "helper":
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            text=text,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query == "close":
        await app.edit_inline_text(callback_query.inline_message_id, "**ᴄʟᴏsᴇ**")
        return
    elif query == "close_help":
        await app.edit_inline_text(
            callback_query.inline_message_id,
            "**ᴄʟᴏsᴇ**",
            reply_markup=InlineKeyboardMarkup(Data.reopen),
        )
        return
    elif query == "closed":
        try:
            await app.delete_messages(callback_query.message.chat.id, callback_query.message.message_id)
        except BaseException:
            pass
    elif query == "make_basic_button":
        try:
            bttn = paginate_help(0, CMD_HELP, "helpme")
            await app.edit_inline_text(
                callback_query.inline_message_id,
                text=text,
                reply_markup=InlineKeyboardMarkup(bttn),
            )
        except Exception as e:
            e = traceback.format_exc()
            print(e, "Callbacks")
    elif query.startswith("helpme_prev"):
        current_page_number = int(re.findall(r'\((.*?)\)', query)[0])
        buttons = paginate_help(current_page_number - 1, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            text=text,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query.startswith("helpme_next"):
        current_page_number = int(re.findall(r'\((.*?)\)', query)[0])
        buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            text=text,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query.startswith("reopen"):
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            text=text,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query.startswith("ub_modul_"):
        modul_name = query.replace("ub_modul_", "")
        commands: dict = CMD_HELP[modul_name]
        this_command = f"**Bantuan Untuk {str(modul_name).upper()}**\n\n"
        for x in commands:
            this_command += f"๏ **Perintah:** `{str(x)}`\n◉ **Keterangan:** `{str(commands[x])}`\n\n"
        this_command += ""
        bttn = [
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="reopen")],
        ]
        reply_pop_up_alert = (
            this_command
            if this_command is not None
            else f"{modul_name} Belum ada penjelasannya ."
        )
        await app.edit_inline_text(
            callback_query.inline_message_id,
            reply_pop_up_alert,
            reply_markup=InlineKeyboardMarkup(bttn),
        )
            

@app.on_callback_query(filters.regex("start_admin"))
async def start_admin(_, query: CallbackQuery):
    ADMIN1 = ADMIN1_ID[0]
    ADMIN2 = ADMIN2_ID[0]
    return await query.edit_message_text(
        f"""<b> ☺️** Silakan hubungi admin dibawah ini jika menemukan kendala.**</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="👮‍♂ Admin 1", user_id=ADMIN1),
                    InlineKeyboardButton(text="👮‍♂ Admin 2", user_id=ADMIN2),
                ],
                  [
                     InlineKeyboardButton(text="Tutup", callback_data="cl_ad"),
                  ],
             ]
        ),
    )


@app.on_callback_query(filters.regex("cl_ad"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
    
@app.on_callback_query(filters.regex("forceclose"))
async def forceclose(_, CallbackQuery):
    try:
        await app.message.delete()
    except:
        pass