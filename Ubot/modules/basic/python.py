
from io import StringIO
from contextlib import redirect_stdout

from pyrogram import Client, filters
from pyrogram.types import Message

from Ubot.core.func import *
from . import *



# noinspection PyUnusedLocal
@Client.on_message(
    filters.command(["ex", "exec", "py", "exnoedit"], cmds) & filters.me
)
def user_exec(client: Client, message: Message):
    if len(message.command) == 1:
        message.edit("<b>Code to execute isn't provided</b>")
        return

    reply = message.reply_to_message

    code = message.text.split(maxsplit=1)[1]
    stdout = StringIO()

    message.edit("<b>Executing...</b>")

    try:
        with redirect_stdout(stdout):
            exec(code)
        text = (
            "<b>Code:</b>\n"
            f"<pre language=python>{code}</pre>\n\n"
            "<b>Result</b>:\n"
            f"<code>{stdout.getvalue()}</code>"
        )
        if message.command[0] == "exnoedit":
            message.reply(text)
        else:
            message.edit(text)
    except Exception as e:
        message.edit(format_exc(e, f"Code was <code>{code}</code>"))



@Client.on_message(filters.command(["ev", "eval"], cmds) & filters.me)
def user_eval(client: Client, message: Message):
    if len(message.command) == 1:
        message.edit("<b>Code to eval isn't provided</b>")
        return

    reply = message.reply_to_message

    code = message.text.split(maxsplit=1)[1]

    try:
        result = eval(code)
        message.edit(
            "<b>Expression:</b>\n"
            f"<pre language=python>{code}</pre>\n\n"
            "<b>Result</b>:\n"
            f"<code>{result}</code>"
        )
    except Exception as e:
        message.edit(format_exc(e, f"Code was <code>{code}</code>"))
