from aiogram import types
from .telegram_bot import dp, bot
from .telegram_supplementary import make_basic_check
from config import TelegramCommands


@dp.message_handler(commands=[TelegramCommands.start, TelegramCommands.help])
async def send_welcome(message:types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    make_basic_check()
    await message.reply("Hello World!")

@dp.message_handler()
async def show_values_message(message:types.Message):
    """
    This message notifier is about the chat if we need chat; 
    need to be commented in cases of the non-usage
    Input:  message = message which user have posted
    Output: None but we have successfully got the chat id
    """
    make_basic_check()
    print(message.chat.id)
    print('######################################')
    print(message)
    print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

async def produce_message_groups(chat_id:int, value_message:str) -> None:
    """
    Method which is dedicated to develop values of the getting messages for all of that
    Input:  chat_id = id of the selected values
            value_message = our message to development
    Output: we have sent the message for the user
    """
    make_basic_check()
    await bot.send_message(chat_id, value_message)
