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

""" MtProto User """

from ast import parse
from pyrogram import (
    Client,
    __version__,
    enums
)
from Ubot.logging import LOGGER
from Ubot import *


class User(Client):
    """ modded client for SessionMakerUser """

    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            in_memory=True,
            parse_mode=enums.ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")


class Userbot(Client):
    def __init__(self):
        self.bot1 = Client(
            name="bot1",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION1,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot2 = Client(
            name="bot2",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION2,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot3 = Client(
          name="bot3",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION3,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot4 = Client(
          name="bot4",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION4,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot5 = Client(
          name="bot5",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION5,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot6 = Client(
          name="bot6",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION6,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot7 = Client(
          name="bot7",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION7,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot8 = Client(
          name="bot8",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION8,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot9 = Client(
          name="bot9",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION9,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot10 = Client(
          name="bot10",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION10,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot11 = Client(
          name="bot11",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION11,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot12 = Client(
          name="bot12",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION12,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot13 = Client(
          name="bot13",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION13,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot4 = Client(
          name="bot14",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION14,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot15 = Client(
          name="bot15",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION15,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot16 = Client(
          name="bot16",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION16,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot17 = Client(
          name="bot17",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION17,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot18 = Client(
          name="bot18",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION18,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot19 = Client(
          name="bot19",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION19,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bot20 = Client(
          name="bot20",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION20,
            in_memory=True,
            
            plugins=dict(root="Ubot/modules"),
        )
        self.bots = [bot for bot in [self.bot1, self.bot2, self.bot3, self.bot4, self.bot5, self.bot6, self.bot7, self.bot8, self.bot9, self.bot10, self.bot11, self.bot12, self.bot17, self.bot18, self.bot19, self.bot20] if bot]
        for bot in self.bots:
            if not hasattr(bot, "group_call"):
                setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())