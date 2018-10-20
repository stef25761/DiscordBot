import re

from utils import UtilsGW2API, UtilsDiscordRoles

utils = UtilsGW2API()
server_Roles = UtilsDiscordRoles()


class Validation():
    # TODO: validate gw2 api key. example at gw2 discord bot github
    # todo: build regex that works :D
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
