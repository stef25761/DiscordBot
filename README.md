# DiscordBot
## install python 3

fist check wicht pythion is installed ( on linux)

```
$ python3 --version
```

If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:

```
$ sudo apt-get update
$ sudo apt-get install python3.6
```
## install pip

```
sudo apt-get install python3-pip
```
## install discord.py framework

```
python3 -m pip install -U discord.py
```
## install gw2Api

```
pip install GuildWars2-API-Client
```
## mongoDb
before install Mongodb, make sure have purged all previous versions, or try to skip it and install the new version
**steps to purge**
```
sudo apt-get purge mongo*
sudo rm -R /var/lib/mongo
```
**try to "force install"**
```
sudo apt-get install -y mongodb-org
```
Start mongo in the shell
```
mongo
```
Now an error appears 
you need
```
sudo systemctl start mongod
sudo systemctl enable mongod
```
**Commands for db**
```
show dbs
use DBNAME
show collections
db.COLLECTIONNAME.find()
```
***MongoDb methods documentation***
```
https://docs.mongodb.com/manual/reference/method/js-collection/
```
## start Bot 
on Linuxserver
```
cd BotDirectory
python3 main.py
```
