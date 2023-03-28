async def addgvar(user_id, variable, value):
    if multi_globals.find_one({"user_id": user_id, "variable": str(variable)}):
        await delgvar(user_id, variable)
    multi_globals.insert_one({"user_id": user_id, "variable": str(variable), "value": value})


async def delgvar(user_id, variable):
    rem = multi_globals.delete_one({"user_id": user_id, "variable": str(variable)})
    if rem:
        return rem.deleted_count


async def gvarstatus(user_id, variable):
    res = multi_globals.find_one({"user_id": user_id, "variable": str(variable)})
    return res["value"] if res else None
    

@Client.on_message(
    filters.private & filters.incoming & ~filters.service & ~filters.me & ~filters.bot
)
async def monito_p_m_s(client, message):
    chat_id = message.chat.id
    user_id = client.me.id
    
    # tambahkan baris berikut
    if not await gvarstatus(str(user_id), "MULTI_MODE"):
        return
    
    botlog_chat_id = await get_botlog(user_id)
    if await gvarstatus(str(user_id), "PMLOG") == "false":
        return
    if not no_log_pms_sql.is_approved(message.chat.id) and message.chat.id != 777000:
        if LOG_CHATS_.RECENT_USER != message.chat.id:
            LOG_CHATS_.RECENT_USER = message.chat.id
            if LOG_CHATS_.NEWPM:
                await LOG_CHATS_.NEWPM.edit(
                    LOG_CHATS_.NEWPM.text.replace(
                        "**💌 PESAN BARU**",
                        f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                    )
                )
                LOG_CHATS_.COUNT = 0
            LOG_CHATS_.NEWPM = await client.send_message(
                botlog_chat_id,
                f"💌 <b><u>MENERUSKAN PESAN BARU</u></b>\n<b> • Dari :</b> {message.from_user.mention}\n<b> • User ID :</b> <code>{message.from_user.id}</code>",
                parse_mode=enums.ParseMode.HTML,
            )
        try:
            async for pmlog in client.search_messages(message.chat.id, limit=1):
                await pmlog.forward(botlog_chat_id)
            LOG_CHATS_.COUNT += 1
        except BaseException:
            pass
