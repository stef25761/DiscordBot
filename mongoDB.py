import pymongo
from utils import Utils
print('Connected to db: '+Utils.MONGO_HOST +':'+ Utils.MONGO_PORT)




class MongoDB(pymongo.MongoClient):

    def __init__(self):
        super(MongoDB, self).__init__(
            host=Utils.MONGO_HOST,port=int(Utils.MONGO_PORT))

    def insertUser(self,user):
        #user is a dictonary of discordname and api key
        self[Utils.DB_NAME][Utils.COLLECTION_NAME].insert_one(user)



    ## maybe dirty, dont know to make it clear
    def getUserList(self):
        userList = []
        for x in self[Utils.DB_NAME].get_collection(Utils.COLLECTION_NAME)\
                .find():
            userList.append(x)
        return userList

    def getUserKey(self, discord_id):

       x = self[Utils.DB_NAME].get_collection(Utils.COLLECTION_NAME) \
           .find({"id":discord_id})
       if x.count() == 1:
           return x[0]["api_key"]


    def getUser(self,discord_id):
        x = self[Utils.DB_NAME][Utils.COLLECTION_NAME] \
                .find({"id": discord_id})
        if x.count() == 1:
            return x[0]["id"]

    def fetchWitchServer(self):
        pass
    def deleteUser(self,discord_id):
      self[Utils.DB_NAME].get_collection(Utils.COLLECTION_NAME)\
        .delete_one({"id": discord_id})

    def printTest(self):
        print("---------")
        if self.getUserList():
            print("in collection user list")
            print(self.getUserList())
        else:
            print("empty List  or no list of user")
        print("---------")
        if self.getUserKey("218419790832861184"):
            print("user apikey")
            print(self.getUserKey("218419790832861184"))
        else:
            print("no user key or user in collection")
        print("---------")
        if self.getUser("218419790832861184"):
            print("user id")
            print(self.getUser("218419790832861184"))
        else:
            print("no user in collection")
        print("---------")








