from aiogram import types
import keyboards.keyboards_generator.user_keyboards as keyboard_generator

from database.db_insert import insert_user
from database.db_get import get_user

async def welcome_user(message: types.Message):
    user_data = await get_user(message.from_user.id)

    if user_data is None:
        await insert_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
        user_data = await get_user(message.from_user.id)

    msg_text = f'Привіт, <b>{user_data["first_name"]}</b>!\n' \
               f'Твоя підгрупа - <b>{user_data["subgroup"]}</b>.\n' \
               f'Ти можеш змінити свою підгрупу, натиснувши на кнопку <b>Змінити підгрупу N</b>.'

    await message.answer(text=msg_text,
                         reply_markup=keyboard_generator.welcome_user())