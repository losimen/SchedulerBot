from aiogram import types


def main_menu(user_data) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    keyboard.add(types.InlineKeyboardButton(text='Змінити підгрупу 1',
                                            callback_data='change_subgroup_1'))
    keyboard.add(types.InlineKeyboardButton(text='Змінити підгрупу 2',
                                            callback_data='change_subgroup_2'))

    keyboard.add(types.InlineKeyboardButton(text='Увімкнути сповіщення' if not user_data['is_notify'] else 'Вимкнути сповіщення',
                                            callback_data='change_notifications' + ('_on' if not user_data['is_notify'] else '_off')))

    return keyboard
