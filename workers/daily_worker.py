import datetime
import asyncio

from loader import bot
from workers import schedule_worker


async def daily_worker():
    await schedule_worker.get_schedule_for_today()

    print(schedule_worker.schedule_for_today)

    while True:
        current_hour_minute = datetime.datetime.now().strftime("%H:%M")
        if current_hour_minute == '00:00':
            await schedule_worker.get_schedule_for_today()

        for lesson in schedule_worker.schedule_for_today:
            if lesson['time'] == current_hour_minute:
                await bot.send_message(chat_id=100, text=f"{lesson['name']}")

        await asyncio.sleep(60)
