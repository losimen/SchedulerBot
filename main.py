import asyncio

from aiogram import Dispatcher, executor
from loader import dp, bot
from config import ADMIN_ID

from database import db_loader

from handlers import user_commands
from FSM import lesson
from workers.daily_worker import daily_worker

user_commands.register_messages_client(dp)
lesson.register_lesson(dp)

async def on_startup(dp: Dispatcher):
    await db_loader.init_db()
    await bot.send_message(chat_id=ADMIN_ID,
                           text="Bot has started")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(daily_worker())

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)