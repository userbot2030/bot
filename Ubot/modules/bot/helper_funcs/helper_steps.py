#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" STEP FIVE """


from telegram import (
    Message
)
from ....my_telegram_org  import *
from Ubot import app
# from telethon import events
# from bot import app


def parse_to_meaning_ful_text(input_phone_number: str, in_dict) -> str:
    """ convert the dictionary returned in STEP FOUR
    into Telegram HTML text """
    me_t = ""
    me_t += "<i>Phone Number</i>: "
    me_t += f"<u>{input_phone_number}</u>"
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>App Configuration</i>"
    me_t += "\n"
    me_t += "<b>APP ID</b>: "
    me_t += "<code>{}</code>".format(in_dict["App Configuration"]["app_id"])
    me_t += "\n"
    me_t += "<b>API HASH</b>: "
    me_t += "<code>{}</code>".format(in_dict["App Configuration"]["api_hash"])
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>Available MTProto Servers</i>"
    me_t += "\n"
    me_t += "<b>Production Configuration</b>: "
    me_t += "<code>{}</code> <u>{}</u>".format(
        in_dict["Available MTProto Servers"]["production_configuration"]["IP"],
        in_dict["Available MTProto Servers"]["production_configuration"]["DC"]
    )
    me_t += "\n"
    me_t += "<b>Test Configuration</b>: "
    me_t += "<code>{}</code> <u>{}</u>".format(
        in_dict["Available MTProto Servers"]["test_configuration"]["IP"],
        in_dict["Available MTProto Servers"]["test_configuration"]["DC"]
    )
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>Disclaimer</i>: "
    me_t += "<u>{}</u>".format(
        in_dict["Disclaimer"]
    )
    return me_t


def extract_code_imn_ges(ptb_message: Message) -> str:
    """ extracts the input message, and returns the
    Telegram Web login code"""
    # initialize a variable that can be used
    # to store the web login code after a
    # sequence of conditionals
    telegram_web_login_code = None
    # the original message text sent by the user
    incoming_message_text = ptb_message
    # lower case can be used as a helper in the
    # comparison logic
    # N.B.: the PASSWORD is case sensitive,
    # so, "telegram_web_login_code" should have the original text,
    # without conversion
    incoming_message_text_in_lower_case = incoming_message_text.lower()
    if "web login code" in incoming_message_text_in_lower_case:
        parted_message_pts = incoming_message_text.split("\n")
        # this logic is deduced by Trial and Error
        if len(parted_message_pts) >= 2:
            telegram_web_login_code = parted_message_pts[1]
            # there might be a better way, but 😐😪😪
    elif "\n" in incoming_message_text_in_lower_case:
        # this condition ideally, should not occur,
        # ("did it come inside this 'elif' ?")
        telegram_web_login_code = None
    else:
        telegram_web_login_code = incoming_message_text
    return telegram_web_login_code


def get_phno_imn_ges(ptb_message: Message) -> str:
    """ gets the phone number (in international format),
    from the input message"""
    my_telegram_ph_no = None
    if ptb_message is not None:
        if len(ptb_message.entities) > 0:
            for c_entity in ptb_message.entities:
                if c_entity.type == "phone_number":
                    my_telegram_ph_no = ptb_message[
                        c_entity.offset:c_entity.length
                    ]
        else:
            my_telegram_ph_no = ptb_message
    elif ptb_message.contact is not None:
        # https://archive.is/X4gsK
        if ptb_message.contact.phone_number != "":
            my_telegram_ph_no = ptb_message.contact.phone_number
    return my_telegram_ph_no



# async def ask(chat_id, text):
#     async with app.conversation(chat_id) as conv:
#         response = conv.wait_event(events.NewMessage(incoming=True, from_users=chat_id))
#         await app.send_message(chat_id, text)
#         response_text = (await response).message.message
#         return response_text

# async def get_otp(message):
#     APP[message.chat.id] = {}
#     await message.reply_text( "Masukan Otp Kedua : " )
#     code = message.text
#     return code
    