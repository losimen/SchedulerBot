import keyboards.keyboards_generator.user_keyboards as keyboard_generator
import datetime
import utils

from aiogram import types

from database.db_insert import insert_user
from database.db_get import get_user, get_schedule_for_weekday

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


async def schedule_menu(message: types.Message):
    weekday = datetime.datetime.today().weekday()
    user_data = await get_user(message.chat.id)
    schedule_today = await get_schedule_for_weekday(weekday)
    msg_text = f'📅 <b>Розклад {utils.convert_weekday_index_to_name(weekday)}:</b>\n'
    for index, lesson  in enumerate(schedule_today):
        if lesson['subgroup'] == user_data['subgroup'] or lesson['subgroup'] == 0:
            msg_text += f'\n{utils.convert_number_to_emoji(index+1)} <b>{lesson["name"]}</b>\n' \
                        f'🎓 {lesson["teacher"]}\n' \
                        f'📝 {utils.convert_lesson_type_to_str(lesson["type"])}  <a href="{lesson["link"]}">Посилання</a>\n' \
                        f'🕒 {lesson["time"]}\n' \
                        '➖➖➖➖➖➖➖➖➖➖'
    # remove last line
    msg_text = msg_text[:msg_text.rfind('\n')]


    await message.answer(text=msg_text)
