from aiogram import types


def welcome_user() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    keyboard.add(types.InlineKeyboardButton(text='Змінити підгрупу 1',
                                            callback_data='change_subgroup_1'))
    keyboard.add(types.InlineKeyboardButton(text='Змінити підгрупу 2',
                                            callback_data='change_subgroup_2'))

    return keyboard
