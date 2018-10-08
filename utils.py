import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')
config_utils = config['Utils']
config_commands = config['Commands_Description']
config_GW2_Api = config['GW2API']
config_server_roles = config['Discord_Server_Roles']
class Utils():
    BOT_TOKEN = config_utils['BOT_TOKEN']
    BOT_DESCRIPTION = config_utils['Bot_Description']
    USER_TOKEN_QUESTION = config_utils['User_Token_Question']
    VALDIDATION_ERROR_MESSAGE = config_utils['Validation_Error_Message']
    BOT_GAME_DESCRIPTION = config_utils['Bot_Game_Description']
    VALIDATE_GW2_API_KEY_ERROR_MESSAGE = config_utils['Validate_Key_Check_GW2_Error_Message']
    API_QUESTION = config_utils['GW2_API_QUESTION']

class UtilsCommand():
    REG = config_commands['REG']
    BE_RUDE = config_commands['BE_RUDE']


class UtilsGW2API():
    HOME_SERVER_ID = int(config_GW2_Api['HOME_SERVER_ID'])
    LINKED_SERVER = int(config_GW2_Api['LINKED_SERVER'])


class UtilsDiscordRoles:
    HOME_SERVER_ROLE = config_server_roles['HOME_SERVER_ROLE']
    LINKED_SERVER_ROLE = config_server_roles['LINKED_SERVER_ROLE']
