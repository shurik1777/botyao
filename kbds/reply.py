from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О магазине'),

        ],
        [
            KeyboardButton(text='Варианты доставки'),
            KeyboardButton(text='Варианты оплаты'),
        ],

    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)

del_kbd = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='О магазине'),
    KeyboardButton(text='Варианты доставки'),
    KeyboardButton(text='Варианты оплаты'),
    KeyboardButton(text='Валюта в рублях'),
    KeyboardButton(text='Бились сражались'),
    KeyboardButton(text='Отнюдь не нужная информация'),
    KeyboardButton(text='Средний класс'),
    KeyboardButton(text='Ежики и Шарфики'),
    KeyboardButton(text='Смурфики и Голубика'),
    KeyboardButton(text='Поднимались тысячу раз'),
    KeyboardButton(text='Средний чек'),
    KeyboardButton(text='Дух борьбы не угас'),
    KeyboardButton(text='woodworking'),
    KeyboardButton(text='Строгий ерш'),
    KeyboardButton(text='То что будет'),
    KeyboardButton(text='Сейчас и здесь'),
    KeyboardButton(text='Не забудет моя земля'),
    KeyboardButton(text='Пала моя империя'),
)
start_kb2.adjust(2, 2)

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text='Оставить отзыв'), )
start_kb3.adjust(2, 2)

test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text='Отправить номер ☎️', request_contact=True),
            KeyboardButton(text='Отправить локацию 🗺️️', request_location=True),
        ],
    ],
    resize_keyboard=True,
)
