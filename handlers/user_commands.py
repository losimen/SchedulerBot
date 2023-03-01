from aiogram import Dispatcher
from menus import user_menus


def register_messages_client(dp: Dispatcher):
    dp.register_message_handler(user_menus.start_menu, commands=['start'])
    dp.register_message_handler(user_menus.create_lesson, commands=['create_lesson'])