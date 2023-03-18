import os
import random
from glob import glob
from pyrogram import Client, filters, types
from pyrogram.errors import PeerIdInvalid
from pyrogram.raw.functions import UploadMediaRequest

from pyrogram.types import InputPeerSelf, InputStickerSetID, InputStickerSetItem
from . import *



async def get_input_documents(client, files):
    inputs = []
    count = 0
    for file in files:
        count += 1
        if file.endswith((".tgs", ".webm")):
            media = await client.send_message("me", file=file)
            inputs.append(
                InputMediaUploadedDocument(
                    file=media.document,
                    mime_type=media.document.mime_type,
                    attributes=media.document.attributes,
                    thumb=media.document.thumb,
                    caption=media.caption
                )
            )
        else:
            inputs.append(
                InputMediaUploadedPhoto(
                    file=await client.upload_media(file),
                    caption=f"Uploaded {file}"
                )
            )
        if count % 5 == 0:
            await client.progress(0, count, f"Uploaded {count} files.")
    return inputs

@Client.on_message(filters.command("packkang", cmds) & filters.me)
async def pack_kangish(client, message):
    _e = message.reply_to_message
    local = None
    try:
        cmdtext = message.text.split(maxsplit=1)[1]
    except IndexError:
        cmdtext = None
    if cmdtext and os.path.isdir(cmdtext):
        local = True
        files = glob(cmdtext + "/*")
        exte = files[-1]
        if exte.endswith(".tgs"):
            typee = "anim"
        elif exte.endswith(".webm"):
            typee = "vid"
        docs = await get_input_documents(client, files)
    elif not (_e and _e.sticker and _e.document.mime_type == "image/webp"):
        return await message.reply_text("Balas pesan stiker atau sertakan direktori yang valid.")
    else:
        docs = []
        try:
            _get_stiks = await client.get_sticker_set(_e.sticker.set_name)
            for i in _get_stiks.documents:
                docs.append(get_input_document(i))
        except PeerIdInvalid:
            return await msg.edit(f"Bot tidak memiliki akses ke set stiker ini.")

    msg = await message.reply_text("Membuat set stiker...")
    _packname = cmdtext or f"Kang Pack By {message.from_user.id}"
    stiks = []
    for i in docs:
        if isinstance(i, InputMediaUploadedPhoto):
            x = await client.send(UploadMediaRequest(InputPeerSelf(), i.file))
            stiks.append(
                InputStickerSetItem(
                    document=x,
                    emoji=random.choice(["😐", "👍", "😂"])
                    if local
                    else (i.caption or "👍"),
                )
            )
        elif isinstance(i, InputMediaUploadedDocument):
            stiks.append(
                InputStickerSetItem(
                    document=i,
                    emoji=random.choice(["😐", "👍", "😂"])
                    if local
                    else (i.caption or "👍"),
                )
            )

    try:
        short_name = "kang_" + _packname.replace(" ", "_") + str(message.message_id)
        _r_e_s = await client.create_sticker_set(
            user_id=message.from_user.id,
            title=_packname,
            name=short_name,
            emojis="👍",
            animated=typee == "anim",
            contains_masks=True,
            stickers=stiks,
        )
    except PeerIdInvalid:
        return await msg.edit(
            f"Hey {message.from_user.mention}, mulailah bot ini terlebih dahulu dan coba perintah ini lagi."
        )
    except Exception as e:
        return await msg.edit(str(e))
    await msg.edit(f"Set stiker {_r_e_s.name} telah berhasil dibuat!\nTambahkan stiker menggunakan @{client.me.username}")
