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
# Use the following method to import the internal module in the current same directory
from . import test_local_external_dotpy
# Import the os module to get the parent path to the local files
import os
# aiofiles module is recommended for file operation
import aiofiles
# You can listen to the interactions.py event
from interactions.api.events import MessageCreate
# You can create a background task
from interactions import Task, IntervalTrigger

'''
Replace the ModuleName with any name you'd like
'''
class MinimalTest(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="a_minimal_test_base",
        description="Replace here for the base command descriptions"
    )
    module_group: interactions.SlashCommand = module_base.group(
        name="a_minimal_test_group",
        description="Replace here for the group command descriptions"
    )

    test_variable=1
    '''
    def __init__(self) -> None:
        self.test_variable:int=1
    '''
    

    @module_group.subcommand("ping", sub_cmd_description="Replace the description of this command")
    @interactions.slash_option(
        name = "option_name",
        description = "Option description",
        required = True,
        opt_type = interactions.OptionType.STRING
    )
    async def module_group_ping(self, ctx: interactions.SlashContext, option_name: str):
        await ctx.send(f"Pong {option_name}!")
        test_local_external_dotpy.external_py_func()

    @module_group.subcommand("print_test_module_variable",sub_cmd_description="Replace the description of this command")
    async def print_test_module_variable(self, ctx: interactions.SlashContext):
        await ctx.send(f"{test_local_external_dotpy.TEST_EXTERNAL_CONSTANT}")

    @module_group.subcommand("print_test_inner_variable",sub_cmd_description="Replace the description of this command")
    async def print_test_module_variable(self, ctx: interactions.SlashContext):
        await ctx.send(f"{self.test_variable}")