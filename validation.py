from utils import UtilsGW2API

utils = UtilsGW2API()
class Validation():
    # TODO: validate gw2 api key. example at gw2 discord bot github
    def validate_token(self, token):
        return len(token) == 59 and \
               token[24] == "." and token[31] == "."

    ##"ABCDE02B-8888-FEBA-1234-DE98765C7DEF" reference key



    def checkServer(self, world_id):
        return world_id == utils.HOME_SERVER_ID or world_id== utils.LINKED_SERVER
