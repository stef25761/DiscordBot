
from gw2api import GuildWars2Client
from validation import Validation
from utils import UtilsGW2API



validation = Validation()
utils = UtilsGW2API()

linked_server_id = utils.LINKED_SERVER

class GW2Api(GuildWars2Client):
    def __init__(self,user_key):
        self.USER_KEY= user_key
        super(GW2Api, self).__init__(api_key = user_key,verify_ssl = False,proxy = None,version = "v2",lang = "en",base_url="https://api.guildwars2.com/")

    def getUserHomeWorld(self):
        return self.account.get().get("world")



