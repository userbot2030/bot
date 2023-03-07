from pyrogram import Client, filters
from Ubot import cmds
from Ubot.modules.basic.help import add_command_help
from ubotlibs import DEVS, ADMINS, BOT_VER, BL_GCAST
from ubotlibs.ubot import Ubot, Devs
add_command_help = add_command_help

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])