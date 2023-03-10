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
import asyncio
from asyncio import gather
from random import choice
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from ubotlibs.ubot.helper import edit_or_reply, get_text, ReplyCheck
from . import *
from ubotlibs.ubot.database.accesdb import *
from config import *


@Ubot("asupan", cmds)
@check_access
async def asupan(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    gz = await edit_or_reply(message, "`mencari asupan...`")
    await gather(
        gz.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

# WARNING PORNO VIDEO THIS !!!

@Ubot("bokep", cmds)
@check_access
async def asupin(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    gz = await edit_or_reply(message, "`Mencari bahan...`")
    await gather(
        gz.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "bahaninimah", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot("ayang", cmds)
@check_access
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await yanto.delete()


@Ubot("ppcp", cmds)
@check_access
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await yanto.delete()
    
    
@Ubot("ppcp2", cmds)
@check_access
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "mentahanppcp", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await yanto.delete()


@Ubot("ppanime", cmds)
@check_access
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await yanto.delete()
    
    
@Ubot("anime", cmds)
@check_access
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "Anime_WallpapersHD", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await yanto.delete()
    
    
@Ubot("bugil", cmds)
@check_access
async def ppanime(client, message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    yanto = await message.reply("🔎 `Search PP Bugil...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "durovbgst", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await yanto.delete()


add_command_help(
    "asupan",[
        [f"asupan", "Asupan video TikTok",],
        [f"ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        [f"ppcp", "Mencari Foto PP Couple Random."],
        [f"ppcp2", "Mencari Foto PP Couple Random 2."],
        [f"bokep", "to send random porno videos."],
        [f"bugil", "to send photo porno random."],
        [f"ppanime", "Mencari Foto PP Couple Anime."],
        [f"anime", "Mencari Foto Anime."],
    ],
)
