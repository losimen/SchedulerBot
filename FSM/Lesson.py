from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton

from database import db_insert


class FSMLesson(StatesGroup):
    save_lesson_name = State()
    save_lesson_link = State()
    save_lesson_subgroup = State()
    save_lesson_is_nominator = State()
    save_lesson_teacher = State()
    save_lesson_type = State()
    save_lesson_week_day = State()
    save_lesson_time = State()


async def fsm_start_lesson(message: types.Message):
    await message.answer('Введіть назву предмету:')
    await FSMLesson.save_lesson_name.set()


async def fsm_lesson_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введіть посилання на предмет:')
    await FSMLesson.next()


async def fsm_lesson_link(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer('Введіть підгрупу (відповідне число):\n\n'
                         '0 - всі підгрупи\n'
                         '1 - 1 підгрупа\n'
                         '2 - 2 підгрупа\n')
    await FSMLesson.next()


async def fsm_lesson_subgroup(message: types.Message, state: FSMContext):
    if message.text not in ['0', '1', '2']:
        await message.answer('Введіть відповідне число!')
        return

    await state.update_data(subgroup=int(message.text))

    await message.answer('Введіть чи є чисельник чи знаменник (відповідне число):\n\n'
                         '0 - всі\n'
                         '1 - чисельник\n'
                         '2 - знаменник\n')
    await FSMLesson.next()


async def fsm_lesson_is_nominator(message: types.Message, state: FSMContext):
    if message.text not in ['0', '1', '2']:
        await message.answer('Введіть відповідне число!')
        return

    await state.update_data(is_nominator=int(message.text))

    await message.answer('Введіть викладача:')
    await FSMLesson.next()


async def fsm_lesson_teacher(message: types.Message, state: FSMContext):
    await state.update_data(teacher=message.text)
    await message.answer('Введіть тип (відповідне число):\n\n'
                         '1. Лекція\n'
                         '2. Практична\n'    
                         '3. Лабораторна\n')

    await FSMLesson.next()


async def fsm_lesson_type(message: types.Message, state: FSMContext):
    if message.text not in ['1', '2', '3']:
        await message.answer('Введіть відповідне число!')
        return

    await state.update_data(type=int(message.text))
    await message.answer('Введіть час (Пн, Вт, Ср, Чт, Пт, Сб, Нд):')
    await FSMLesson.next()


async def fsm_lesson_week_day(message: types.Message, state: FSMContext):
    weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
    if message.text not in weekdays:
        await message.answer('Введіть відповідний тиждень!')
        return

    await state.update_data(week_day=weekdays.index(message.text))
    await message.answer('Введіть час (приклад 14:00):')
    await FSMLesson.next()


async def fsm_lesson_time(message: types.Message, state: FSMContext):
    try:
        datetime.strptime(message.text, '%H:%M')
    except ValueError:
        await message.answer('Введіть відповідний час!')
        return

    await state.update_data(time=message.text)
    await db_insert.insert_lesson(await state.get_data())
    await message.answer('Успішно створено!')

    await state.finish()


def register_lesson(dp: Dispatcher):
    dp.register_message_handler(fsm_start_lesson, commands=['create_lesson'])
    dp.register_message_handler(fsm_lesson_name, state=FSMLesson.save_lesson_name)
    dp.register_message_handler(fsm_lesson_link, state=FSMLesson.save_lesson_link)
    dp.register_message_handler(fsm_lesson_subgroup, state=FSMLesson.save_lesson_subgroup)
    dp.register_message_handler(fsm_lesson_is_nominator, state=FSMLesson.save_lesson_is_nominator)
    dp.register_message_handler(fsm_lesson_teacher, state=FSMLesson.save_lesson_teacher)
    dp.register_message_handler(fsm_lesson_type, state=FSMLesson.save_lesson_type)
    dp.register_message_handler(fsm_lesson_week_day, state=FSMLesson.save_lesson_week_day)
    dp.register_message_handler(fsm_lesson_time, state=FSMLesson.save_lesson_time)
