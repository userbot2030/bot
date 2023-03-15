# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/xtsea

import os
import requests
import random
import json
import asyncio
from pyrogram import Client, filters
from pyrogram.types import *

from . import * 

# isi var sini

API_KEY_GOOGLE = None
SEARCH_ENGINE_ID = None 

search_params = {
    'q': '',
    'num': 1,
    'imgSize': 'large',
    'imgType': 'photo',
    'searchType': 'image'
}

@Ubot("gimage", cmds)
async def api_google_image(c: Client, m: Message):
    if len(m.command) == 1:
       await m.reply_text(f"Example: `+{m.command[0]} pocong`\n\n**untuk pencarian khusus gambar google lainnya**")
       return

    search_term = m.text.split(" ", 1)[1]
    api_key = API_KEY_GOOGLE
    search_engine_id = SEARCH_ENGINE_ID
    if not api_key and not search_engine_id:
       await m.reply_text("missing api key : `API_KEY_GOOGLE` and `SEARCH_ENGINE_ID`")
       return

    search_params['q'] = search_term
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}'
    response = requests.get(url, params=search_params)
    response_json = response.json()

    if "items" in response_json and len(response_json['items']) > 0:
        image_url = response_json['items'][0]['link']
        wtf = await m.reply_text("Uploading....")
        await asyncio.sleep(2)
        google_caption = f"**Powered By** {c.me.mention}"
        await c.send_photo(m.chat.id, image_url, caption=google_caption, reply_to_message_id=m.id)
    else:
        await wtf.edit_text("No results found for your search query.")
    try:
        await wtf.delete()
    except Exception:
        pass
