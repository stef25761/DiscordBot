# Work with Python 3.6
import random

import discord
from discord import Game
from discord.ext import commands

from gw2ApiKey import GW2Api
from utils import Utils, UtilsCommand, UtilsDiscordRoles
from validation import Validation

utils = Utils()
description = utils.BOT_DESCRIPTION
askForAPIKey = utils.API_QUESTION
command_description = UtilsCommand()
server_roles = UtilsDiscordRoles()

validation = Validation()
class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", description=description, pm_help=None, has_permission=8)
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
   #TODO: Add user to the correct serverrole
    @commands.command(description=command_description.REG,pass_context=True)
    @commands.bot_has_permissions(administrator=True)
    async def reg(self,ctx):
        msg = askForAPIKey
        await self.send_message(ctx.message.author, msg)
        user_message = await self.wait_for_message(author=ctx.message.author)
        user = ctx.message.author
        home_roles = discord.utils.get(user.server.roles, name=server_roles.HOME_SERVER_ROLE)


        try:
            gw2API = GW2Api(user_message.content)
            id = gw2API.getUserHomeWorld()

            if validation.checkServer(id):
                print(user)
                print(home_roles)

                await self.add_roles(user, home_roles)
                await self.send_message(ctx.message.author, "Danke. Wirst gerade hinzugefügt")
            else:
                await self.send_message(ctx.message.author, "Du bist leider nicht auf Kodash oder dem gelinktem Server")
        except:
            await self.send_message(ctx.message.author,
                                    "Bitte verwende noch einmal den Befehl !reg im DiscordChatChannel"
                                    "Da ein Fehler aufgetaucht ist")





    @commands.command(description = command_description.BE_RUDE,pass_context=True)
    async def be_rude(self,context):
        possible_brainfarts = ["Du Stinkst", "Geh dich Erhängen",
                               "Deine Mudda sammelt hässliche Kinder!",
                               "Ich kann schneller Radfahren als du!",
                               "Dein Atem stinkt nach Pimmel", "Du Spermadose",
                               "Du Eselarschfetischist","Du Hurrenküsser",
                               "Du Ziegenwämser","Flischentischbesitzer!!"
                               ]
        await self.say(random.choice(
            possible_brainfarts) + ", " + context.message.author.mention)
    ##endregion




