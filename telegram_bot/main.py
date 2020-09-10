import logging
from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin, skip_updates=True)




