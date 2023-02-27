from loader import dp, logger
from aiogram.dispatcher.filters import Text
from menus import user_menus
from aiogram import types

from database.db_update import update_user_group, update_user_notifications


@dp.callback_query_handler(text = 'void')
async def void_call(callback: types.CallbackQuery):
    pass


@dp.callback_query_handler(Text(startswith = 'change_subgroup_'))
async def change_subgroup(callback: types.CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass

    subgroup_number = callback.data.split('_')[-1]
    await update_user_group(callback.message.chat.id, subgroup_number)

    await user_menus.main_menu(callback.message)


@dp.callback_query_handler(Text(startswith = 'change_notifications_'))
async def change_notifications(callback: types.CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass

    is_notify = True if callback.data.split('_')[-1] == 'on' else False

    await update_user_notifications(callback.message, is_notify)
    await user_menus.main_menu(callback.message)

