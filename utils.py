import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')
config_utils = config['Utils']
config_commands = config['Commands_Description']
config_GW2_Api = config['GW2API']
config_server_roles = config['Discord_Server_Roles']
config_error_messages = config['ErrorMessages']

class Utils():
    BOT_TOKEN = config_utils['BOT_TOKEN']
    BOT_DESCRIPTION = config_utils['Bot_Description']
    USER_TOKEN_QUESTION = config_utils['User_Token_Question']
    BOT_GAME_DESCRIPTION = config_utils['Bot_Game_Description']
    API_QUESTION = config_utils['GW2_API_QUESTION']
    WELCOME_MSG =config_utils['WELCOME_MSG']
    ADD_USER_TO_ROLE_MSG = config_utils['ADD_USER_TO_ROLE_MSG']
    IN_WORK = config_utils['IN_WORK']
class UtilsCommand():
    REG = config_commands['REG']
    BE_RUDE = config_commands['BE_RUDE']


class UtilsGW2API():
    HOME_SERVER_ID = int(config_GW2_Api['HOME_SERVER_ID'])
    LINKED_SERVER = int(config_GW2_Api['LINKED_SERVER'])


class UtilsDiscordRoles:
    HOME_SERVER_ROLE = config_server_roles['HOME_SERVER_ROLE']
    LINKED_SERVER_ROLE = config_server_roles['LINKED_SERVER_ROLE']

class ErrorMessages:
    VALDIDATION_ERROR_MESSAGE = config_error_messages['Validation_Error_Message']
    VALIDATE_GW2_API_KEY_ERROR_MESSAGE = config_error_messages[
        'Validate_Key_Check_GW2_Error_Message']
    USER_IS_IN_ROLE = config_error_messages['USER_IS_IN_ROLE']
    UPPS_THER_IS_WAS_WRONG = config_error_messages['UPPS_THER_IS_WAS_WRONG']