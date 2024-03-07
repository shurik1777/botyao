import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message()
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


async def on_startup():
    await dp.start_polling(bot)


asyncio.run(on_startup())
