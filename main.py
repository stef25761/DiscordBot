from bot import DiscordBot
from utils import Utils, ErrorMessages
from validation import Validation


validation= Validation()
utils= Utils()
error_message = ErrorMessages ()
bot_token = utils.BOT_TOKEN

while not validation.validate_token(bot_token):
    print(error_message.VALDIDATION_ERROR_MESSAGE)
    userInput = input(utils.USER_TOKEN_QUESTION)


bot= DiscordBot()
bot.run(bot_token)
