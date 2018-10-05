from bot import DiscordBot
from utils import Utils
from validation import Validation


validation= Validation()
utils= Utils()
userInput = input(utils.USER_TOKEN_QUESTION)

while not validation.validateToken(userInput):
    print(utils.VALDIDATION_ERROR_MESSAGE)
    userInput = input(utils.USER_TOKEN_QUESTION)


bot= DiscordBot()
bot.description = input(utils.BOT_DESCRIPTION)
bot.run(userInput)




