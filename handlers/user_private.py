from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')


@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню: ")


@user_private_router.message(Command('about'))
async def menu_about(message: types.Message):
    await message.answer("О нас: ")


# @user_private_router.message(Command('recap'))
# async def menu_recap(message: types.Message):
#     await message.answer("Актуальное за 3 дня: ")


@user_private_router.message(Command('payment'))
async def menu_about(message: types.Message):
    await message.answer("Варианты оплаты: ")


@user_private_router.message(Command('shipping'))
async def menu_about(message: types.Message):
    await message.answer("Варианты доставки: ")


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
"""
