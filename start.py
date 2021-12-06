import time
import asyncio
import schedule
from pprint import pprint
from aiogram import executor
from datetime import datetime
from telegram.telegram_bot import dp, bot
from telegram.telegram_ui import produce_message_groups
from telegram.telegram_supplementary import make_basic_check
from utilities.telegram_utilities import (return_value_json,
                                        return_datetime_day, 
                                        return_datetime_hour)
from config import MessageJson, MessageJson


async def make_group_values_message(loop, value_start:int=1) -> set:
    """
    Function which is dedicated to get required values
    """
    make_basic_check()
    value_json = return_value_json()
    
    datetime_now = datetime.now()
    datetime_day = return_datetime_day(datetime_now)
    datetime_hour = return_datetime_hour(datetime_now)
    hour_start, hour_finished = value_json.get('Days', {}).get(datetime_day, [0, 0])
    if hour_start < datetime_hour < hour_finished:
        value_bool = 'true' if datetime_day == MessageJson.true_value else 'false'
        value_message_sent = value_json.get('Messages', {}).get(value_bool, [])
        if not value_message_sent:
            return
        value_message_sent = value_message_sent[value_start]
        for chat_id in value_json.get('Groups', []):
            await produce_message_groups(chat_id, value_message_sent)
    return 

def make_hour_experiment(value_stop=1):
    """
    Main function which is dedicated to work with values
    Input:  value_stop = value which means the stop values
    """
    loop = asyncio.get_event_loop()
    executor.start(dp, make_group_values_message(loop, value_stop), skip_updates=True)

if __name__ == '__main__':
    schedule.every().hour.at(MessageJson.minutes_allow).do(make_hour_experiment, (0))
    schedule.every().hour.at(MessageJson.minutes_disable).do(make_hour_experiment, (1))
    while True:
        schedule.run_pending()
        time.sleep(1)