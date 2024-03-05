import asyncio

from aiogram import Bot, Dispatcher, types

bot = Bot(token='')
dp = Dispatcher()


@dp.message()
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


async def on_startup():
    await dp.start_polling(bot)


asyncio.run(on_startup())
