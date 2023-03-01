from aiogram import types
import keyboards.keyboards_generator.user_keyboards as keyboard_generator

from database.db_insert import insert_user
from database.db_get import get_user

async def start_menu(message: types.Message):
    if message.chat.type != 'private':
        return

    user_data = await get_user(message.chat.id)
    if user_data is None:
        await insert_user(message.from_user.id, message.chat.id, message.from_user.first_name)

    await main_menu(message)


async def main_menu(message: types.Message):
    user_data = await get_user(message.chat.id)
    msg_text = f'👋 Привіт, <b>{user_data["first_name"]}</b>!\n\n' \
               f'👥 Твоя підгрупа - <b>{user_data["subgroup"]}</b>.\n' \
               f'🔔 Отримувати сповіщення: <b>{"Так" if user_data["is_notify"] else "Ні"}</b>.\n\n'

    await message.answer(text=msg_text,
                         reply_markup=keyboard_generator.main_menu(user_data))
