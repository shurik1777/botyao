import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv
from aiogram.filters import CommandStart

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Это была команда старт')


@dp.message()
async def echo(message: types.Message) -> None:
    await message.answer(message.text)
    await message.reply(message.text)


async def on_startup() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(on_startup())
