from loader import dp, logger
from aiogram.dispatcher.filters import Text
from menus import user_menus
from aiogram import types

from database.db_update import update_user_group


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
    await update_user_group(callback.from_user.id, subgroup_number)

    await user_menus.welcome_user(callback.message)
