import pymongo
from utils import Utils

print('Connected to db: ' + Utils.MONGO_HOST + ':' + Utils.MONGO_PORT)


class MongoDB(pymongo.MongoClient):

    def __init__(self):
        super(MongoDB, self).__init__(
            host=Utils.MONGO_HOST, port=int(Utils.MONGO_PORT))

    def create_collection(self, discord_server_name):
        self[discord_server_name]

    def insertUser(self, user, collection_name):
        # user is a dictonary of discordname and api key
        self[Utils.DB_NAME][collection_name].insert_one(user)

    ## maybe dirty, dont know to make it clear
    def getUserList(self, collection_name):
        userList = []
        for x in self[Utils.DB_NAME].get_collection(collection_name) \
                .find():
            userList.append(x)
        return userList

    def getUserKey(self, discord_id, collection_name):

        x = self[Utils.DB_NAME].get_collection(collection_name) \
            .find({"id": discord_id})
        if x.count() == 1:
            return x[0]["api_key"]

    def getUser(self, discord_id, collection_name):

        x = self[Utils.DB_NAME][collection_name] \
            .find({"id": discord_id})
        if x.count() == 1:
            return x[0]["id"]

    def get_server_from_user(self, discord_id, collection_name):
        x = self[Utils.DB_NAME][collection_name] \
            .find({"id": discord_id})
        if x.count() == 1:
            return x[0]["discord_server_id"]

    def fetchWitchServer(self):
        pass

    def deleteUser(self, discord_id, collection_name):
        self[Utils.DB_NAME].get_collection(collection_name) \
            .delete_one({"id": discord_id})


