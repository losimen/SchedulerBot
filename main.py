from aiogram import Dispatcher, executor
from loader import dp, bot
from config import ADMIN_ID
from handlers import user_commands

from database import db_loader


user_commands.register_messages_client(dp)

async def on_startup(dp: Dispatcher):
    await db_loader.init_db()
    await bot.send_message(chat_id=ADMIN_ID,
                           text="Bot has started")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)