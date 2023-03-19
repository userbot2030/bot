import asyncio
from threading import Event

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from ubotlibs.ubot.helper.basic import edit_or_reply
from ubotlibs.ubot.utils.misc import extract_args
from . import *
from config import BOTLOG_CHATID
from ubotlibs.ubot.database.accesdb import *


SPAM_COUNT = [0]

commands = ["spam", "statspam", "slowspam", "fspam"]

def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()


def spam_allowed():
    return SPAM_COUNT[0] < 1000


@Ubot("dspam", cmds)
async def delayspam(client: Client, message: Message):
    #if message.chat.id in BL_GCAST:
    #    return await edit_or_reply(
    #        message, "**Gabisa Digunain Disini Tod!!**"
    #    )
    delayspam = await extract_args(message)
    arr = delayspam.split()
    if len(arr) < 3 or not arr[0].isdigit() or not arr[1].isdigit():
        await message.edit("`Something seems missing / wrong.`")
        return
    delay = int(arr[0])
    count = int(arr[1])
    spam_message = delayspam.replace(arr[0], "", 1)
    spam_message = spam_message.replace(arr[1], "", 1).strip()
    await message.delete()

    if not spam_allowed():
        return

    delaySpamEvent = Event()
    for i in range(0, count):
        if i != 0:
            delaySpamEvent.wait(delay)
        await client.send_message(message.chat.id, spam_message)
        limit = increment_spam_count()
        if not limit:
            break

    await client.send_message(
        BOTLOG_CHATID, "**#DELAYSPAM**\nDelaySpam was executed successfully"
    )


@Ubot(commands, cmds)
async def sspam(client, message):
    amount = 1
    text = ""

    # check if the command is replying to a message
    replied_message = message.reply_to_message
    if replied_message:
        replied_text = replied_message.text
    else:
        # check if the command has a custom text to spam
        args = message.text.split(maxsplit=1)[1:]
        if args:
            text = args[0]
        else:
            await message.reply_text("You need to reply to a message or provide a custom text to spam.")
            return

    # set the cooldown for each type of spam
    cooldown = {"spam": 0.15, "statspam": 0.5, "slowspam": 0.9, "fspam": 0.5}

    # delete the command message
    await message.delete()

    # loop to send the spam messages
    for i in range(amount):
        if text:
            # if custom text is provided, send it
            sent = await client.send_message(message.chat.id, text)
        else:
            # if replying to a message, send the same message
            sent = await replied_message.reply(replied_text)

        # apply the appropriate cooldown for the spam type
        await asyncio.sleep(cooldown[message.command[0]])

        # delete the message for statspam type
        if message.command[0] == "statspam":
            await sent.delete()




@Ubot("sspam", cmds)
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await edit_or_reply(
            message, "**Reply to a sticker with amount you want to spam**"
        )
        return
    if not message.reply_to_message.sticker:
        await edit_or_reply(
            message, "**Reply to a sticker with amount you want to spam**"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)

add_command_help(
    "spam",
    [
        ["spam <jumlah spam> <text>", "Mengirim teks secara spam dalam obrolan!!"],
        ["fspam <jumlah spam> <text>", "Mengirim spam secara cepat dalam obrolan!!"],
        [f"dspam [jumlah] [waktu delay] [kata kata]","Delay spam.",],
        [f"sspam [balas ke stiker] [jumlah spam]","Spam stiker.",],
    ],
)
