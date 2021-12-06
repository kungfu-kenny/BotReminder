import os
from dotenv import load_dotenv

load_dotenv()

class FileSystem:
    folder = 'storage'
    folder_present = os.getcwd()
    file_present = 'input_message.json'

class TelegramSystem:
    token = os.getenv('TOKEN')
    admin = os.getenv('ID_ADMIN')
    receivers = [] #TODO you need to add 

class TelegramCommands:
    start = 'start'
    help = 'help'

class MessageJson:
    true_value = 'Wednesday'
    minutes_allow = ':50'
    minutes_disable = ':00'
    dictionary_part_day_lang = {
        False:[
            "You can have break for now",
            "Please, let's keep quiet this time"
        ],
        True: [
            'Адкрыў варкатанне',
            'Ахапіла варкатанне'
        ],
    }
    dictionary_part_day = {
        'Monday':[9, 20],
        'Tuesday': [9, 20],
        'Wednesday': [9, 20],
        'Thursday': [9, 20],
        'Friday': [9, 18],
    }
