# Work with Python 3.6
import random

import discord
from discord import Game
from discord.ext import commands

from utils import Utils, UtilsGW2API, UtilsCommand
from validation import Validation

description =""
askForAPIKey="Einfach den API Key mir schicken und " \
             "dann wirst du zugeorndet! Bitte warten :P"
command_description = UtilsCommand()
utils = Utils()
utils_gw2_api_key = UtilsGW2API()
validation = Validation()
class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",description=description,pm_help=None)
        self.add_command(self.be_rude)
        self.add_command(self.reg)


    ## region events
    async def on_ready(self):
        await self.change_presence(game=Game(name=utils.BOT_GAME_DESCRIPTION))
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        print(discord.__version__)



    async def on_member_join(self,user):
        # TODO: bot commands or direct registration
        try:
            msg = askForAPIKey
            user_message = await self.wait_for_message(author=user)
            print(user_message.content)
            await self.send_message(user, msg)

        except:
            print("on_member_join dont work")



    async def on_member_remove(self,user):
        #TODO: Server owener pm, that someone leaves, delete his role in db or delete total
        try:
            msg = "und Tschö"
            await self.send_message(user, msg)

        except:
            print("on_member_remove dont work")


    ## endregion

    ##region Bot commands
    # TODO: initial gw2 api here
    @commands.command(description=command_description.REG,pass_context=True)
    async def reg(self,ctx):
        msg = askForAPIKey
        await self.send_message(ctx.message.author, msg)
        user_message = await self.wait_for_message(author=ctx.message.author)

        while not validation.validate_gw2_api_token(user_message.content):
            await  self.send_message(ctx.message.author, utils.VALIDATE_GW2_API_KEY_ERROR_MESSAGE)
            user_message = await  self.wait_for_message(author=ctx.message.author)

        if validation.validate_gw2_api_token(user_message.content):
            utils_gw2_api_key = user_message.content
            ##gw2API = gw2ApiKe
            await self.send_message(ctx.message.author, "Vielen dank, deine Anfrage wird bearbeitet")
        print(utils_gw2_api_key)




    @commands.command(description = command_description.BE_RUDE,pass_context=True)
    async def be_rude(self,context):
        possible_brainfarts = ["Du Stinkst", "Geh dich Erhängen",
                               "Deine Mudda sammelt hässliche Kinder!",
                               "Ich kann schneller Radfahren als du!"]
        await self.say(random.choice(
            possible_brainfarts) + ", " + context.message.author.mention)
    ##endregion




