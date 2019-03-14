import re

from mongoDB import MongoDB
from utils import UtilsGW2API, UtilsDiscordRoles

utils = UtilsGW2API()
server_Roles = UtilsDiscordRoles()


class Validation():

    def validate_token(self, token):
        return len(token) == 59 and \
               token[24] == "." and token[31] == "."

    def checkHomeServer(self, world_id):

        return world_id == utils.HOME_SERVER_ID

    def checkLinkedServer(self, world_id):
        return world_id == utils.LINKED_SERVER

    def checkGW2APIKey(self, key):
        regex = "([A-Z,0-9]){8}-(([A-Z,0-9]){4}-){3}([A-Z,0-9]){20}-(([A-Z,0-9]){4}-){3}([A-Z,0-9]){12}"
        return re.match(regex, key) and len(key) == 72

    def checkUserExist(self, discord_id):
        return discord_id == MongoDB.getUser(discord_id)

    def user_in_role(self, user, home_role, linked_role):
        return (str(home_role) in [y.name for y in user.roles]) or \
               (str(linked_role) in [y.name for y in user.roles])
