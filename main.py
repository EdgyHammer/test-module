'''
Discord-Bot-Module template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/

Copyright (C) 2024  __retr0.init__

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import interactions
from interactions import Client, Intents
from interactions import Message
from interactions import Extension, BaseContext, listen
from interactions import ActionRow, Button, ButtonStyle
from interactions import Modal, ShortText, ModalContext
from interactions import SlashCommand, SlashContext
from interactions.api.events import Component, ThreadCreate, MessageReactionAdd
from interactions.models.discord.channel import GuildForum, GuildForumPost
from enum import IntEnum
from typing import List, Dict
import json
import aiofiles
import asyncio
import datetime
import os
import re

from . import test_utils


'''
Replace the ModuleName with any name you'd like
'''
class TestModule(interactions.Extension):
    def __init__(self, bot: Client):
        self.bot: Client = bot

        # self.COMPETITION_THREAD_ID: int = 1228196847668170812

        self.channel: GuildForum = None
        self.control_panel: test_utils.ControlPanel = None

    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="replace_your_command_base_here",
        description="Replace here for the base command descriptions"
    )

    @module_base.subcommand(sub_cmd_name='test', sub_cmd_description='test command, for test only')
    async def test(self, ctx: SlashContext):
        self.control_panel.print_competition_info()

    @module_base.subcommand(sub_cmd_name='setup_competition', sub_cmd_description='Set up the competition bet environments.')
    async def setup_competition(self, ctx: SlashContext):
        self.channel = self.bot.get_channel(test_utils.COMPETITION_FORUM_CHANNEL_ID)
        print(self.channel)
        self.control_panel = test_utils.ControlPanel(self.channel)
        await self.control_panel.create_control_panel_thread()

