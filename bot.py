# Work with Python 3.6
import asyncio
import random

import discord
from discord import Game
from discord.ext import commands

import validation
from gw2ApiKey import GW2Api
from mongoDB import MongoDB
from utils import Utils, UtilsCommand, UtilsDiscordRoles, ErrorMessages
from validation import Validation

utils = Utils()
description = utils.BOT_DESCRIPTION
askForAPIKey = utils.API_QUESTION
command_description = UtilsCommand()
server_roles = UtilsDiscordRoles()
error_messages = ErrorMessages()
validation = Validation()
mongoDb = MongoDB()


class DiscordBot(commands.Bot):
    # old but u run the bot only on one server, its fine
    # current_server_joined = None

    def __init__(self):
        super().__init__(command_prefix="!", description=description,
                         pm_help=True, has_permission=8,
                         status=discord.Status.idle)
        self.add_command(self.be_rude)
        self.add_command(self.reg)

    # region events
    async def on_server_join(self, server):
        print("create server collection")
        mongoDb.create_collection(server.name)
        print("---------------------------------")
        print("join server: " + str(server.name))
        print("server id: " + str(server.id))
        print("---------------------------------")

    async def on_ready(self):
        await self.change_presence(game=Game(name=utils.BOT_GAME_DESCRIPTION))

        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        # works for only one server Q.Q
        # print('Logged on Server')
        # if self.is_logged_in:
        # channel_list = list(self.get_all_channels())

        # if self.current_server_joined:
        # self.current_server_joined = channel_list[0].server
        # print(self.current_server_joined.name)
        # print('-------')
        # else:
        # print("no server connected")
        print(discord.__version__)

    async def on_member_join(self, user):
        msg = utils.WELCOME_MSG
        await self.send_message(user, msg)

    async def backgoundTask(self):
        await self.wait_until_ready()

        while not self.is_closed:

            # if u run the bot on one server, u dont need the for loop.
            # refactor all server with current_server_joined.
            # normally its works well
            counter = 0

            server_list = self.servers
            for server in server_list:
                userList = mongoDb.getUserList(server.name)
                print("collection size: " + str(len(userList)))
                print("------------------------")
                counter += 1
                print("|server: " + str(counter))
                if userList:

                    for userObject in userList:

                        userID = userObject["id"]
                        userKey = userObject["api_key"]
                        user_membership_server_id = userObject[
                            "discord_server_id"]
                        userWorld = int(userObject["home_server"])

                        if server is not None:
                            user = server.get_member(str(userID))
                            home_role = UtilsDiscordRoles.HOME_SERVER_ROLE
                            linked_role = UtilsDiscordRoles.LINKED_SERVER_ROLE

                            if (validation.checkHomeServer(userWorld)):

                                if not validation.user_in_role(user, home_role,
                                                               linked_role):
                                    await self.add_roles(user, home_role)
                                else:
                                    print("|-------------------")
                                    print("|user: " + str(user))
                                    print("|user id: " + str(userID))
                                    print("|user key: " + str(userKey))
                                    print("|-------------------")
                                    print("|guild wars 2 server id: " + str(
                                        userWorld))
                                    print("|discord server id: " + str(
                                        user_membership_server_id))
                                    print("|-------------------")
                            elif validation.checkLinkedServer(userWorld):
                                if not validation.user_in_role(user, home_role,
                                                               linked_role):
                                    await  self.add_roles(user, linked_role)
                                else:
                                    print("|-------------------")
                                    print("|user: " + str(user))
                                    print("|user id: " + str(userID))
                                    print("|user key: " + str(userKey))
                                    print("|-------------------")
                                    print("|guild wars 2 server id: " + str(
                                        userWorld))
                                    print("|discord server id: " + str(
                                        user_membership_server_id))
                                    print("|-------------------")

                            else:
                                mongoDb.deleteUser(userID, server.name)
                                print(server.get_member(str(userID)))
                                user = server.get_member(str(userID))
                                userRoleHomeServer = None
                                userRole = discord.utils.get(
                                    user.server.roles,
                                    name=server_roles.HOME_SERVER_ROLE)
                                if userRole.name == server_roles.HOME_SERVER_ROLE:
                                    userRoleHomeServer = userRole
                                elif userRole.name == server_roles.LINKED_SERVER_ROLE:
                                    userRoleHomeServer = userRole

                                await self.remove_roles(
                                    server.get_member(str(userID)),
                                    userRoleHomeServer)
                        else:
                            print("bot isn't on a server. "
                                  "Please join him to a server")
                else:
                    print("Db is empty")
                ##await asyncio.sleep(int(utils.CHECK_INTERVALL))

            await asyncio.sleep(int(utils.CHECK_INTERVALL))

    ## endregion

    ##region Bot commands

    @commands.command(description=command_description.REG, pass_context=True)
    async def reg(self, ctx):
        msg = askForAPIKey
        await self.send_message(ctx.message.author, msg)

        user_message = await self.wait_for_message(author=ctx.message.author)
        user = ctx.message.author
        server_name = user.server.name
        user_api_key = mongoDb.getUserKey(user.id, server_name)
        server_id = user.server.id
        server_of_membership = mongoDb.get_server_from_user(user.id,
                                                            server_name)

        home_roles = discord.utils.get(user.server.roles,
                                       name=server_roles.HOME_SERVER_ROLE)
        linked_roles = discord.utils.get(user.server.roles,
                                         name=server_roles.LINKED_SERVER_ROLE)

        if (
                validation.user_in_role(ctx.message.author, home_roles,
                                        linked_roles)):
            await self.send_message(ctx.message.author,
                                    utils.ADD_USER_TO_ROLE_MSG)

        elif ((str(user_message.content) == str(user_api_key) and
               str(server_id) == str(server_of_membership))):
            await self.send_message(ctx.message.author,
                                    utils.ADD_USER_TO_ROLE_MSG)
        else:
            try:
                gw2API = GW2Api(user_message.content)

                id = gw2API.getUserHomeWorld()
                __name = gw2API.get_account_name()
                if validation.checkHomeServer(id):

                    await self.add_roles(user, home_roles)
                    await self.send_message(ctx.message.author,
                                            utils.IN_WORK)
                    __userDic = {
                        "id": user.id,
                        "acc_name": __name,
                        "api_key": user_message.content,
                        "home_server": id,
                        "discord_server_id": user.server.id
                    }

                    mongoDb.insertUser(__userDic, user.server.name)

                elif (validation.checkLinkedServer(id)):

                    await self.add_roles(user, linked_roles)
                    await self.send_message(ctx.message.author,
                                            utils.IN_WORK)
                    __userDic = {
                        "id": user.id,
                        "acc_name": __name,
                        "api_key": user_message.content,
                        "home_server": id,
                        "discord_server_id": user.server.id
                    }

                    mongoDb.insertUser(__userDic, user.server.name)
                else:
                    await self.send_message(ctx.message.author,
                                            error_messages.USER_IS_IN_ROLE)
            except:
                await self.send_message(ctx.message.author,
                                        error_messages.UPPS_THER_IS_WAS_WRONG)

    @commands.command(description=command_description.BE_RUDE,
                      pass_context=True)
    async def be_rude(self, context):
        possible_brainfarts = [""
                               ]
        await self.say(random.choice(
            possible_brainfarts) + ", " + context.message.author.mention)
    ##endregion
