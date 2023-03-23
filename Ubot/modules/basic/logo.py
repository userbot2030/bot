# Credits : @Xtsea

from . import *

from Ubot.core.lgs import *

@Ubot("logo", "")

async def logo_command(client, message):

    await logo_write(client, message)

add_command_help(
    "logo",
    [
        [f"logo [kata]", "Buat Logo Secara Random."],
        [f"logo2 [kata]", "Buat Logo Secara Random."],
    ],
)
