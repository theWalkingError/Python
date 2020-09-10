from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# buttons
web_scrapper = KeyboardButton('Web Scrapper')
git_hub_button = KeyboardButton('Git Hub')
stack_button = KeyboardButton('StackOverflow')
useful_button = KeyboardButton('Полезные функции')

cancel_button = KeyboardButton('Отмена')
input_login_git = KeyboardButton('Ввести логин')

location_button = KeyboardButton('Местоположение', request_location=True)
contact_button = KeyboardButton('Номер \nтелефона', request_contact=True)

location_number_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(location_button)

markup_git_input = ReplyKeyboardMarkup(resize_keyboard=True).row(input_login_git, cancel_button)

markup1 = ReplyKeyboardMarkup(resize_keyboard=True).row(git_hub_button, stack_button).add(useful_button)
markup2 = ReplyKeyboardMarkup(resize_keyboard=True).add(stack_button)


# inline buttons
cancel_inline_button = InlineKeyboardButton('Отмена', callback_data='cancel')
authorize_inline_button = InlineKeyboardButton('Авторизация', callback_data='authorize') 
git_hub_inline_button = InlineKeyboardButton('💻 Репозитории', url="https://github.com/theWalkingError?tab=repositories")
git_hub_inline_button_1 = InlineKeyboardButton('🗿 Профиль', url='https://github.com/theWalkingError')
# inline_keyboard_1 = InlineKeyboardMarkup().row(git_hub_inline_button, git_hub_inline_button_1)
inline_keyb = InlineKeyboardMarkup( 
    inline_keyboard=
    [
        [
            git_hub_inline_button, git_hub_inline_button_1
        ], 
        [
            authorize_inline_button
        ]
    ]
)
