from aiogram import Bot, Dispatcher
from config import TelegramSystem


bot = Bot(token=TelegramSystem.token)
dp = Dispatcher(bot)