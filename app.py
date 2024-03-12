"""Точка входа начиная с 3-й лекции"""
import asyncio
from os import getenv  # Переделал под pycharm в виртуальное окружение

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
from handlers.user_private import user_private_router

load_dotenv(find_dotenv())


ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=getenv('TOKEN'))  # Тоже редакция вместо os.getenv - сразу getenv
dp = Dispatcher()

dp.include_router(user_private_router)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
