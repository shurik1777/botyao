"""Точка входа начиная с 3-й лекции"""
import asyncio
from os import getenv  # Переделал под pycharm в виртуальное окружение
from aiogram.client.bot import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import find_dotenv, load_dotenv

from handlers.user_group import user_group_router
from handlers.user_private import user_private_router
from handlers.admin_private import admin_router

from common.bot_cmds_list import private, private2
load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Тоже редакция вместо os.getenv - сразу getenv
# bot = Bot(token=getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Понадобится при смене версии на 3.5.0
# так же нужно будет импортировать этот метод прямо с aiogram , сейчас он тут from aiogram.client.bot import DefaultBotProperties
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
