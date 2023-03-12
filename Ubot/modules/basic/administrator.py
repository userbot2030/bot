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
from time import time
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from . import *
from ubotlibs.ubot.utils.misc import *
from ubotlibs.ubot.helper import *
from ubotlibs.ubot.database.accesdb import *



unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(filters.command("setgpic", cmds) & filters.me)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("Kamu tidak punya akses wewenang")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("Balas ke photo untuk set!")



@Client.on_message(filters.command("ban", cmds) & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("Tidak dapat menemukan pengguna.")
    if user_id == client.me.id:
        return await rd.edit("Tidak bisa banned diri sendiri.")
    if user_id in DEVS:
        return await rd.edit("Tidak bisa banned Devs!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("Tidak bisa banned admin.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    msg = f"**Banned User:** {mention}\n**Banned By:** {message.from_user.mention}\n"
    if reason:
        msg += f"**Reason:** {reason}"
    try:
        await message.chat.ban_member(user_id)
        await rd.edit(msg)
    except ChatAdminRequired:
        return await rd.edit("**Anda bukan admin di group ini !**")



@Client.on_message(filters.command("unban", cmds) & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    rd = await message.reply("`Processing...`")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await rd.edit("Tidak bisa unban ch")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await rd.edit(
            "Berikan username, atau reply pesannya."
        )
    try:
        await message.chat.unban_member(user)
        umention = (await client.get_users(user)).mention
        await rd.edit(f"Unbanned! {umention}")
    except ChatAdminRequired:
        return await rd.edit("**Anda bukan admin di group ini !**")



@Client.on_message(filters.command(["pin", "unpin"], cmds) & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await message.edit_text("Balas ke pesan untuk pin/unpin .")
    rd = await message.reply("`Processing...`")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await rd.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await rd.edit(
            f"**Pinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        return await rd.edit("**Anda bukan admin di group ini !**")


@Client.on_message(filters.command("mute", cmds) & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("Pengguna tidak ditemukan.")
    if user_id == client.me.id:
        return await rd.edit("Tidak bisa mute diri sendiri.")
    if user_id in DEVS:
        return await rd.edit("Tidak bisa mute dev!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("Tidak bisa mute admin.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Reason:** {reason}"
    try:
        await message.chat.restrict_member(user_id, permissions=ChatPermissions())
        await rd.edit(msg)
    except ChatAdminRequired:
        return await rd.edit("**Anda bukan admin di group ini !**")



@Client.on_message(filters.command("unmute", cmds) & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("Pengguna tidak ditemukan.")
    try:
        await message.chat.restrict_member(user_id, permissions=unmute_permissions)
        umention = (await client.get_users(user_id)).mention
        await rd.edit(f"Unmuted! {umention}")
    except ChatAdminRequired:
        return await rd.edit("**Anda bukan admin di group ini !**")


@Client.on_message(filters.command("kick", cmds) & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("Pengguna tidak ditemukan.")
    if user_id == client.me.id:
        return await rd.edit("Tidak bisa kick diri sendiri.")
    if user_id == DEVS:
        return await rd.edit("Tidak bisa kick dev!.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("Tidak bisa kick admin.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await rd.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await rd.edit("**Anda bukan admin di group ini !**")


@Client.on_message(filters.command("promote", cmds) & filters.me)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("Pengguna tidak ditemukan.")
    rd = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try: 
        if message.command[0][0] == "f":
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                ),
            )
            return await rd.edit(f"Fully Promoted! {umention}")

        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        await rd.edit(f"Promoted! {umention}")
    except ChatAdminRequired:
        return await rd.edit("**Anda bukan admin di group ini !**")


@Client.on_message(filters.command("demote", cmds) & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("Pengguna tidak ditemukan")
    if user_id == client.me.id:
        return await rd.edit("Tidak bisa demote diri sendiri.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await rd.edit(f"Demoted! {umention}")


add_command_help(
    "admin",
    [
        [f"ban [reply/username/userid]", "Ban pengguna."],
        [f"unban [reply/username/userid]", "Unban pengguna.",],
        [f"kick [reply/username/userid]", "kick pengguna dari group."],
        [f"promote `or` .fullpromote","Promote pengguna.",],
        [f"demote", "Demote pengguna."],
        [f"mute [reply/username/userid]","Mute pengguna.",],
        [f"unmute [reply/username/userid]","Unmute someone.",],
        [f"pin [reply]","to pin any message.",],
        [f"unpin [reply]","To unpin any message.",],
        [f"setgpic [reply ke image]","To set an group profile pic",],
    ],
)
