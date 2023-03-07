from pyrogram import Client, filters
from Ubot import cmds
from Ubot.modules.basic.help import add_command_help

add_command_help = add_command_help

BOT_VER = "7.2.0"


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])