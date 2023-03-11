
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
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ppcp...`")
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
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ppcp 2...`")
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
    
    
@Ubot("anime", cmds)
@check_access
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Anime...`")
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
    
   
@Ubot("anime2", cmds)
@check_access
async def ayang(client, message):
    
    yanto = await message.reply("🔎 `Search Anime...`")
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
        [f"anime", "Mencari Foto PP Couple Anime."],
        [f"anime2", "Mencari Foto Anime."],
    ],
)
