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

import os
from pyrogram import filters, Client
from pyrogram.types import Message
from py_trans import Async_PyTranslator
from ubotlibs.ubot.helper.utility import get_arg
from . import *
from googletrans import Translator
from ubotlibs.ubot.database.accesdb import *

@Ubot("tr", cmds)
@check_access
async def translate(client: Client, message: Message):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        input_str = (
            message.text.split(None, 1)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        target = input_str or "id"
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message.edit(
                f"**ERROR:** `{str(err)}`",
                parse_mode=enums.ParseMode.MARKDOWN,
            )
            return
    else:
        input_str = (
            message.text.split(None, 2)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        text = message.text.split(None, 2)[2]
        target = input_str or "id"
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message.edit(
                "**ERROR:** `{}`".format(str(err)),
                parse_mode=enums.ParseMode.MARKDOWN,
            )
            return
    await message.edit(
        f"**Diterjemahkan ke:** `{target}`\n```{tekstr.text}```\n\n**Bahasa yang Terdeteksi:** `{(await trl.detect(text))}`",
        parse_mode=enums.ParseMode.MARKDOWN,
    )

add_command_help(
    "translate",
    [
        [f"tr", "Menerjemahkan teks ke bahasa yang disetel. (Default kode bahasa Indonesia)."],
        [f"tr <kode bahasa>", "Menyetel kode bahasa"],
        [f"voicelang", "Untuk mengetahui kode bahasa"],
    ],
)
