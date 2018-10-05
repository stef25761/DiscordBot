from gw2api import GuildWars2Client

from utils import UtilsGW2API
# test = GuildWars2Client(api_key="hierKönnteDeinTokenStehen")
# print(dir(test))
# acc = test.account.get()
# print(acc)
# print(acc.get("world"))
from validation import Validation

validation = Validation()
utils = UtilsGW2API()
# user_key = utils.USER_API_KEY
user_key = ""


class GW2Api(GuildWars2Client):
    def __init__(self):
        self.api_key = user_key
        self.verify_ssl = False
        self.proxy = None
        self.version = "2"
        self.lang = "eng"

    def getWorld(self):
        print(dir(self))
    # acc = self.account.get()
    # if validation.checkServer(acc.get("world")):
    #   print("Korrekt")
    # else:
    #   print("Nicht Korrekt")


client = GW2Api()
client.getWorld()
