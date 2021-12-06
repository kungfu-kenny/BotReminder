import os
import json
from datetime import datetime
from config import FileSystem


def check_presence_folder(path_folder:str) -> None:
    """
    Function to check folder present
    Input:  path_folder = path of the folder which is going to get checked
    Output: we created this folder in this cases
    """
    os.path.exists(path_folder) or os.mkdir(path_folder)

def check_presence_file(path_file:str) -> bool:
    """
    Function to check file presence in the system
    Input:  path_file = full path to the file
    Output: boolean value of the presence of this file
    """
    return os.path.exists(path_file) and os.path.isfile(path_file)

def check_presence_file_ext(path_file:str) -> bool:
    """
    Function to check extention of selected files
    Input:  path_file = path to the file which would be developed
    Output: boolean value of the extention of the values
    """
    return os.path.splitext(path_file)[1].lower() == ".json"

def return_datetime_day(datetime_now:object=datetime.now()) -> str:
    """
    Function which is dedicated to return value of the day
    Input:  datetime_now = datetime value which is checked
    Output: we returned with selected format values
    """
    return datetime_now.strftime('%A')

def return_datetime_hour(datetime_now:object=datetime.now()) -> int:
    """
    Function which is dedicated to return our hour in the int parameter to check
    Input:  datetime_now = datetime value which is checked
    Output: we returned value of the hoys    
    """
    return datetime_now.hour

def return_value_json() -> dict:
    """
    Function which is dedicated to return values of the json values
    Input:  None
    Output: we returned dictionary with required values
    """
    with open(
        os.path.join(
            FileSystem.folder_present, 
            FileSystem.folder, 
            FileSystem.file_present
        ), 'r') as json_file:
        return_json = json.load(json_file)
    return return_json