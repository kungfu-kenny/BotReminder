import os
import json
from utilities.telegram_utilities import (check_presence_folder, 
                                        check_presence_file,
                                        check_presence_file_ext)
from config import (FileSystem, 
                    MessageJson, 
                    TelegramSystem)


def check_presence_json() -> bool:
    """
    Function which is dedicated to check presence of the json presented within the file system
    Input:  None
    Output: boolean check of the presented file within the file system
    """
    check_presence_folder(
        os.path.join(
            FileSystem.folder_present, 
            FileSystem.folder)
        )
    file_present = os.path.join(
            FileSystem.folder_present, 
            FileSystem.folder, 
            FileSystem.file_present)
    return check_presence_file(file_present) \
        and check_presence_file_ext(file_present)

def produce_development_json() -> None:
    """
    Function which is dedicated to create the json values in this cases 
    Input:  None
    Output: we developed values of the Json values
    """
    file_json_path = os.path.join(
        FileSystem.folder_present, 
        FileSystem.folder, 
        FileSystem.file_present)
    with open(file_json_path, 'w') as file_json:
        json.dump(
            {   
                "Groups": TelegramSystem.receivers,
                "Days": MessageJson.dictionary_part_day, 
                "Messages": MessageJson.dictionary_part_day_lang
            }, 
            file_json, 
            sort_keys = False, 
            indent = 4)

def make_basic_check() -> None:
    """
    Function which is dedicated to work with json creation
    Input:  None
    Output: We produced json values for the basic usage
    """
    if not check_presence_json():
        produce_development_json()