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
from asyncio import sleep
import os
from . import *
from ubotlibs.ubot.utils.misc import *
from ubotlibs.ubot.helper.PyroHelpers import ReplyCheck
from pyrogram import Client, filters
from pyrogram.types import Message

from ubotlibs.ubot.database.accesdb import *

flood = {}
profile_photo = "cache/pfp.jpg"



@Ubot("unblock", cmds)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await message.edit(
            "Berikan username atau reply pesan untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await tex.edit("Ok done ✅.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil membuka blokir** {umention}")


@Ubot("block", cmds)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await tex.edit_text(
            "Berikan username untuk di blok."
        )
    if user_id == client.me.id:
        return await tex.edit_text("ok ✅.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**Berhasil mem-blokir** {umention}")


@Ubot("setname", cmds)
async def setname(client: Client, message: Message):
    tex = await message.reply_text("`Processing . . .`")
    if len(message.command) == 1:
        return await tex.edit(
            "Berikan text untuk diatur sebagai nama anda."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(f"**Berhasil mengganti nama menjadi** `{name}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit(
            "Berikan text untuk diatur sebagai nama anda."
        )


@Ubot("setbio", cmds)
async def set_bio(client: Client, message: Message):
    tex = await message.edit_text("`Processing . . .`")
    if len(message.command) == 1:
        return await tex.edit("Berikan text untuk diatur sebagai bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"**Berhasil mengganti bio menjadi** `{bio}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit("Berikan text untuk diatur sebagai bio.")

@Ubot("setpp", cmds)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        profile_photo = profile_photo
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("**Foto profil berhasil di ganti.**")
    else:
        await message.reply_text(
            "Balas ke gamabr/foto untuk atur sebagai foto profil"
        )
        await sleep(3)
        await message.delete()




add_command_help(
    "profile",
    [
        [f"block", "Blokir pengguna"],
        [f"unblock", "membuka blokir"],
        [f"setname", "mengatur nama anda."],
        [f"setbio", "mengatur bio anda."],
        
    ],
)
