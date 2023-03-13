"""
✅ Edit Code Boleh
❌ Hapus Credits Jangan

👤 Telegram: @T0M1_X
"""

import datetime
from asyncio import get_event_loop

import wget
from Ubot import app, cmds
from ubotlibs.ubot import Ubot
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL


def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))


def YouTubeSearch(query):
    search = VideosSearch(query, limit=1).result()
    data = search["result"][0]
    videoid = data["id"]
    title = data["title"]
    duration = data["duration"]
    url = f"https://youtu.be/{videoid}"
    views = data["viewCount"]["text"]
    channel = data["channel"]["name"]
    thumbnail = data["thumbnails"][0]["url"].split("?")[0]
    return [videoid, title, duration, url, views, channel, thumbnail]


@Ubot("Tomi_Vid", cmds)
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>Video tidak ditemukan,</b>\nmohon masukan judul video dengan benar.",
        )
    infomsg = await message.reply_text("<b>🔍 Pencarian...</b>", quote=False)
    try:
        search = YouTubeSearch(message.text.split(None, 1)[1])
    except Exception as error:
        return await infomsg.edit(error)
    link = search[3]
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    try:
        ytdl_data = await run_sync(ydl.extract_info, link, download=True)
        file_path = ydl.prepare_filename(ytdl_data)
    except Exception as error:
        return await infomsg.edit(error)
    videoid = ytdl_data["id"]
    title = ytdl_data["title"]
    url = f"https://youtu.be/{videoid}"
    duration = ytdl_data["duration"]
    channel = ytdl_data["uploader"]
    views = f"{ytdl_data['view_count']:,}".replace(",", ".")
    thumbs = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    file_name = file_path
    thumbnail = wget.download(thumbs)
    audio_or_video = "video"
    await client.send_video(
        message.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption="<b>💡 Informasi {}</b>\n\n<b>🏷 Nama:</b> {}\n<b>🧭 Durasi:</b> {}\n<b>👀 Dilihat:</b> {}\n<b>📢 Channel:</b> {}\n<b>🔗 Tautan:</b> <a href={}>Youtube</a>\n\n<b>⚡ Powered By:</b> {}".format(
            audio_or_video,
            title,
            datetime.timedelta(seconds=duration),
            views,
            channel,
            url,
            app.me.mention,
        ),
        reply_to_message_id=message.id,
    )
