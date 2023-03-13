import io
from io import *
import os
import requests
import openai
import shutil
import random
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from . import *
from Ubot.modules.basic.dev import *
from ubotlibs.ubot.database.accesdb import *
from asyncio import gather

import httpx
from aiohttp import ClientSession

# Aiohttp Async Client
session = ClientSession()

# HTTPx Async Client
http = httpx.AsyncClient(
    http2=True,
    timeout=httpx.Timeout(40),
)

RMBG_API_KEY = "3RCCWg8tMBfDWdAs44YMfJmC"

OPENAI_API_KEY = "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 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".split()

API = "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"


async def get(url: str, *args, **kwargs):
    async with session.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def head(url: str, *args, **kwargs):
    async with session.head(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def post(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def multiget(url: str, times: int, *args, **kwargs):
    return await gather(*[get(url, *args, **kwargs) for _ in range(times)])


async def multihead(url: str, times: int, *args, **kwargs):
    return await gather(*[head(url, *args, **kwargs) for _ in range(times)])


async def multipost(url: str, times: int, *args, **kwargs):
    return await gather(*[post(url, *args, **kwargs) for _ in range(times)])


async def resp_get(url: str, *args, **kwargs):
    return await session.get(url, *args, **kwargs)


async def resp_post(url: str, *args, **kwargs):
    return await session.post(url, *args, **kwargs)

# cradit: Tomi Setiawan > @T0M1_X
class OpenAi:
    def Text(question):
        openai.api_key = random.choice(OPENAI_API_KEY)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Q: {question}\nA:",
            temperature=0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text

    def Photo(question):
        openai.api_key = random.choice(OPENAI_API_KEY)
        response = openai.Image.create(prompt=question, n=1, size="1024x1024")
        return response["data"][0]["url"]
        

@Ubot(["ai", "ask"], cmds)
async def openai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"Ketik <code>{prefix}{m.command[0]} [question]</code> Pertanyaan untuk menggunakan OpenAI")
    question = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 500,
        "temperature": 0,
    }
    msg = await m.reply("`Processing..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("`Data tidak ditemukan, pastikan OPENAI_API valid...`")


@Ubot(["img", "photo"], cmds)
async def img(client, message):
    Tm = await message.reply("<code>Memproses...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b><code>{message.text}</code> [query]</b>")
    try:
        response = OpenAi.Photo(message.text.split(None, 1)[1])
        msg = message.reply_to_message or message
        await message.reply_photo(message.chat.id, response, reply_to_message_id=msg.id)
        return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()
        
@Ubot("rmbg", cmds)
async def rmbg_background(c: Client, m: Message):
    api_key = RMBG_API_KEY
    reply = m.reply_to_message
    ky = await m.reply("`Processing..")
    photo_id = m.reply_to_message.photo.file_id
    if not (reply and (reply.media)):
      return await m.edit("`Mohon balas ke foto...`")
    temp_file = await c.download_media(photo_id)
    if not api_key:
       return await m.edit("**RMBG_API_KEY: missing**")
    endpoint = "https://api.remove.bg/v1.0/removebg"
    payload = {"size": "auto"}

    if api_key:
       with open(temp_file, "rb") as image_file:
          response = requests.post(endpoint, data=payload, headers={"X-Api-Key": api_key}, files={"image_file": image_file}, stream=True)

    with open("output.png", "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    await m.reply_document("output.png")
    try:
       clear_file = "ky.webp"
       clear_file2 = "output.png"
       (await shell_exec("cp *.png ky.webp"))[0]
       await c.send_sticker(m.chat.id, "ky.webp")
       os.remove(clear_file)
       os.remove(clear_file2)
    except BaseException:
        pass


add_command_help(
    "openai",
    [
        [f"ask or ai [pertanyaan]", "Chat Open AI."],
    ],
)

add_command_help(
    "image",
    [
        [f"img or photo [query]", "Untuk mengunduh gambar yang dicari."],
        [f"rmbg [reply photo]", "Untuk menghapus background pada gambar."],
        [f"toanime <reply to foto>", "Convert foto ke anime menggunakan ai bot"],
        [f"toimg <reply stiker>", "Convert stiker ke foto."],
    ],
)
