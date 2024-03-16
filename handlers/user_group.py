from string import punctuation
from aiogram import types, Router
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'кабан', 'хомяк', 'выхухоль'}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))  # метод, который чистит текст от пунктуации


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f'{message.from_user.first_name}, соблюдайте порядок в чате!')
        await message.delete()  # Удаляет слова из списка
        # await.chat.ban(message.from_user.id)  # Можно банить по id
