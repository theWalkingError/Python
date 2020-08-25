import logging
from config import *

from aiogram import Bot, Dispatcher, executor, types

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравствуйте, хозяйн! Я Ваш персональный бот. Исполню любое ваше пожелание.")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Список команд, которые я могу исполнить:")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)