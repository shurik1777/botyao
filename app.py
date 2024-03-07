import asyncio
import os  # импортирована как зависимость для dotenv-python

from aiogram import Bot, Dispatcher, types  # Все те 1е импорты без которых не будут работать самые первые шаги
from dotenv import find_dotenv, load_dotenv  # Тут импортировал библиотеку для того, что бы спрятать токен
from aiogram.filters import \
    CommandStart  # Через фильтры импортируем специальный класс который указывает хендлеру кого поедать

"""Ниже две строки отвечают 1е за подгрузку локальную токена через который БОТ подключается к API телеграмма"""
load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()  # Обработчик - как КПП или Дверь обрабатывает все что прилетает от бота


# @dp.message()  # Символ ЭД = @ - собака! ХЭндлер с пустым значением в скобках - будет реагировать на все события отправленные ему
@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:  # Пишем хендлер который будет хватать розовой шупальцой событие
    await message.answer('Это была команда старт')


@dp.message()  # Нужно учитывать очередность в системе фильтрации
async def echo(message: types.Message) -> None:
    text: str | None = message.text
    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer('И тебе привет!')
    elif text in ['Пока', 'пока', 'пакеда', 'До свидания']:
        await message.answer('И тебе покеда!')
    else:
        await message.answer(message.text)


async def on_startup() -> None:  # Все функции асинхронны ходят по кругу и не ждут очередь на выполнения
    await dp.start_polling(bot)


asyncio.run(on_startup())
