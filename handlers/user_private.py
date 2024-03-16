from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')


# @user_private_router.message(Command('menu'))
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))  # or_f - функция или
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню: ')


@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def menu_about(message: types.Message):
    await message.answer('О нас: ')


@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def menu_about(message: types.Message):
    await message.answer('Варианты оплаты: ')


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))  # логическое ИЛИ сработает или на то или на это
@user_private_router.message(Command('shipping'))
async def menu_about(message: types.Message):
    await message.answer('Варианты доставки: ')


# @user_private_router.message(F.text, F.text.lower() == "варианты доставки")  # Если оба условия равно логическое И
# async def menu_about(message: types.Message):
#     await message.answer("This magik")

"""
Что бы в самом боте настроить кнопки меню нужно пройти определенный алгоритм:
1. Для удобства создать папку с https://t.me/BotFather и своим ботом чатами для удобной работы
2. Зайдя в настройку своего бота Меню /mybots выбрать нужного
3. Жмем Edit Bot, жмем Edit Commands
4. Настраиваем его меню - тут самое главное это символ разделитель '-' слева должно быть слово menu справа описание, 
что данная кнопка при нажатии будет выводить(выполнять в общении с ботом)
5. Методом проб и ошибок - добиваемся нужного результата!
6. Что бы добавить актуальность сразу нескольких меню нужно в ботфазер вводить таким образом
start - start
menu - menu
about - about
recap - recap
7. Можно не пользоваться методом выше, а передавать списком все выше написанное, это
лишь 2 варианта из 3х возможных
"""
