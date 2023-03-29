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
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION1,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot2 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION2,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot3 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION3,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot4 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION4,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot5 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION5,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot6 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION6,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot7 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION7,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot8 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION8,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot9 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION9,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot10 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION10,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot11 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION11,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot12 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION12,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot13 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION13,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot4 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION14,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot15 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION15,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot16 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION16,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot17 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION17,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot18 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION18,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot19 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION19,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bot20 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=SESSION20,
            in_memory=True,
            cache_duration=100,
            plugins=dict(root="Ubot/modules"),
        )
        self.bots = [bot for bot in [self.bot1, self.bot2, self.bot3, self.bot4, self.bot5, self.bot6, self.bot7, self.bot8, self.bot9, self.bot10, self.bot11, self.bot12, self.bot17, self.bot18, self.bot19, self.bot20] if bot]
        for bot in self.bots:
            if not hasattr(bot, "group_call"):
                setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())