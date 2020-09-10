from main import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from config import admin_id
from keybords import *
from webscraper_bot import rep_count, rep_names
from urllib.error import HTTPError, URLError
from states import Test
from aiogram.dispatcher import FSMContext

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Здравствуйте, хозяйн! Что вы хотите сделать?", reply_markup=markup1)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Список команд, которые я могу исполнить:") 

@dp.message_handler(text='Git Hub')
async def git_click(message: types.Message):
    await message.answer('Твой аккаунт Git Hub', reply_markup=inline_keyb)

@dp.callback_query_handler(Text(equals='authorize'))
async def cancel_button(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Для авторизации необходимо ввести логин Git Hub:')
    
    @dp.message_handler()
    async def echo(message: types.Message):
        git_login = message.text
        try:
            repos_number = rep_count(git_login) 
            repos_names = rep_names(git_login)
            await message.answer(f'Твой логин: {git_login}\nКоличество публичных репозиториев: {repos_number}')

            repos_list = list()
            for name in repos_names: 
                repos_list.append(name)
            await message.answer(f'Репозитории: {repos_list}')
            
        except HTTPError as error:
            await message.answer('Ошибка, проверьте правильность написания логина')


@dp.message_handler(text='Полезные функции')
async def useful_func(message: types.Message):
    await message.answer('Здесь вы можете узнать свое местоположение', reply_markup=location_number_keyboard)
    





