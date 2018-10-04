# Work with Python 3.6
import random

import discord
from discord import Game
from discord.ext import commands

from DiscordBot.utils import Utils_Command

description =""
askForAPIKey="Einfach den API Key mir schicken und " \
             "dann wirst du zugeorndet! Bitte warten :P"
command_description = Utils_Command()
class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",description=description,pm_help=None)
        self.add_command(self.be_rude)
        self.add_command(self.reg)


    ## region events

    async def on_ready(self):
        await self.change_presence(game=Game(name="Warten auf Anweisungen,Master!"))
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        print(discord.__version__)



    async def on_member_join(self,user):
        try:
            msg = askForAPIKey
            await self.send_message(user, msg)
        except:
            pass



    async def on_member_remove(self,user):
        try:
            msg = "und Tschö"
            await self.send_message(user, msg)

        except:
            pass


    ## endregion

    ##region Bot commands
    @commands.command(description=command_description.REG,pass_context=True)

    async def reg(self,ctx):
        msg = askForAPIKey
        await self.send_message(ctx.message.author, msg)



    @commands.command(description = command_description.BE_RUDE,pass_context=True)
    async def be_rude(self,context):
        possible_brainfarts = ["Du Stinkst", "Geh dich Erhängen",
                               "Deine Mudda sammelt hässliche Kinder!",
                               "Ich kann schneller Radfahren als du!"]
        await self.say(random.choice(
            possible_brainfarts) + ", " + context.message.author.mention)
    ##endregion




