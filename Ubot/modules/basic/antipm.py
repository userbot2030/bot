# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team


from ubotlibs.ubot.utils.tools import get_arg
from pyrogram import filters, Client
from pyrogram.types import Message
from . import *
from Ubot.core.db.pmpermit import *
from Ubot.core.db import pmpermit as set

PM_LOGGER = 1
FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}


async def denied_users(filter, client, message):
    user_id = client.me.id
    if not await pm_guard(user_id):
        return False
    if message.chat.id in (await get_approved_users(user_id)):
        return False
    else:
        return True


@Ubot("pmguard", "")
async def pm_permit(client, message):
    arg = get_arg(message)
    user_id = client.me.id
    if not arg:
        await message.edit("**on atau off ??**")
        return
    if arg == "off":
        await set.set_pm(user_id, False)
        await message.edit("**PM Guard Dimatikan**")
    if arg == "on":
        await set.set_pm(user_id, True)
        await message.edit("**PM Guard diaktifkan**")
        
@Ubot("setpmmsg", "")
async def setpmmsg(client, message):
    arg = get_arg(message)
    user_id = client.me.id
    if not arg:
        await message.edit("**berikan pesan untuk set**")
        return
    if arg == "default":
        await set.set_permit_message(user_id, set.PMPERMIT_MESSAGE)
        await message.edit("**pesan Anti PM diset ke default**.")
        return
    await set.set_permit_message(f"`{arg}`")
    await message.edit("**Pesan custom Anti Pm diset**")

@Ubot("setlimit", "")
async def pmguard(client, message):
    user_id = client.me.id
    arg = get_arg(message)
    if not arg:
        await message.edit("**Set limit to what?**")
        return
    await set.set_limit(user_id, int(arg))
    await message.edit(f"**Limit set to {arg}**")



@Ubot("setblocking", "")
async def setpmmsg(client, message):
    user_id = client.me.id
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await set.set_block_message(user_id, BLOCKED)
        await message.edit("**Block message set to default**.")
        return
    await set.set_block_message(f"`{arg}`")
    await message.edit("**Custom block message set**")

File "/root/bot/Ubot/modules/basic/antipm.py", line 97, in allow
    pmpermit, pm_message, limit, block_message = await get_pm_settings(user_id)
TypeError: cannot unpack non-iterable bool object

@Client.on_message(filters.command(["allow", "ok", "approve", "k"], "") & filters.me & filters.private)
async def allow(client, message):
    user_id = client.me.id
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await get_pm_settings(user_id)
    await set.allow_user(user_id, chat_id)
    await message.edit(f"**Menerima pesan dari [Anda](tg://user?id={chat_id}).**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@Client.on_message(filters.command(["deny", "fuck", "no", "blok"], "") & filters.me & filters.private)
async def deny(client, message):
    user_id = client.me.id
    chat_id = message.chat.id
    await set.deny_user(user_id, chat_id)
    await message.edit(f"**Saya belum menyetujui [Anda](tg://user?id={chat_id}) untuk mengirim pesan.**")


@Client.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
)
async def reply_pm(client, message):
    user_id = client.me.id
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await set.get_pm_settings(user_id)
    user = message.from_user.id
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]
    
    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return
        async for message in client.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await message.delete()
        await message.reply(pm_message, disable_web_page_preview=True)
        return
    await message.reply(block_message, disable_web_page_preview=True)
    await client.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})

add_command_help(
    "pm",
    [
        [f"pmguard [on or off]", " -> mengaktifkan dan menonaktifkan anti-pm."],
        [f"setpmmsg [message or default]", " -> Sets a custom anti-pm message."],
        [f"setblockmsg [message or default]", "-> Sets custom block message."],
        [f"setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [f"ok", " -> Allows a user to PM you."],
        [f"no", " -> Denies a user to PM you."],
    ],
)