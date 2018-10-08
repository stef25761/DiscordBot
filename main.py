from bot import DiscordBot
from utils import Utils
from validation import Validation


validation= Validation()
utils= Utils()
bot_token = utils.BOT_TOKEN

while not validation.validate_token(bot_token):
    print(utils.VALDIDATION_ERROR_MESSAGE)
    userInput = input(utils.USER_TOKEN_QUESTION)


bot= DiscordBot()
bot.run(bot_token)
