#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys

from os import execle
from dotenv import load_dotenv, set_key


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors import (
    SessionPasswordNeeded,
    BadRequest
)
from .start import restart
from Ubot.user import User
from Ubot import (
    ACC_PROK_WITH_TFA,
    AKTIFPERINTAH,
    PHONE_CODE_IN_VALID_ERR_TEXT,
    RECVD_PHONE_CODE,
    SESSION_GENERATED_USING,
    ALREADY_REGISTERED_PHONE,
    CONFIRM_SENT_VIA,
    RECVD_PHONE_NUMBER_DBP,
    app
)

load_dotenv()

NUM_SESSIONS = 100

@app.on_message(filters.text & filters.private, group=2)
async def recv_tg_code_message(client, message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    sent_code = w_s_dict.get("SENT_CODE_R")
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    if not sent_code or not phone_number:
        return
    status_message = w_s_dict.get("MESSAGE")
    if not status_message:
        return
    del w_s_dict["MESSAGE"]
    phone_code = "".join(message.text.split(" "))
    try:
        w_s_dict["SIGNED_IN"] = await loical_ci.sign_in(
            phone_number,
            sent_code.phone_code_hash,
            phone_code
        )
    except BadRequest as e:
        await status_message.edit_text(
            e.MESSAGE + "\n\n" + PHONE_CODE_IN_VALID_ERR_TEXT
        )
        del AKTIFPERINTAH[message.chat.id]
    except SessionPasswordNeeded:
        await status_message.edit_text(
            "Verifikasi 2 Langkah diaktifkan, mohon masukkan kode verifikasi 2 langkah anda..",
        )
        w_s_dict["IS_NEEDED_TFA"] = True
    else:
        session_string = await loical_ci.export_session_string()
        for session_num in range(1, NUM_SESSIONS+1):
            if not os.getenv(f"SESSION{session_num}"):
                with open(".env", "a") as f:
                    f.write(f"SESSION{session_num}={session_string}\n")
                await message.reply_text(
                    SESSION_GENERATED_USING, quote=True
                )
                break
        del AKTIFPERINTAH[message.chat.id]
        return False
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation()











