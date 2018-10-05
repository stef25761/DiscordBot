from utils import UtilsGW2API

utils = UtilsGW2API()
class Validation():
    # TODO: validate gw2 api key
    def validate_token(self, token):
        return len(token) == 59 and \
               token[24] == "." and token[31] == "."

    ##"ABCDE02B-8888-FEBA-1234-DE98765C7DEF" reference key

    def validate_gw2_api_token(self, token):
        return len(token) == 36 and token[8] == "-" and token[13] == "-" and \
               token[18] == "-" and token[23] == "-"

    def checkServer(self, world_id):
        return world_id == utils.KODASH_ID
