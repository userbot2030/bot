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


from .apm import get_arg
from pyrogram import filters, Client
from pyrogram.types import Message
from . import *
from Ubot.core.db import pmpermit as set

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