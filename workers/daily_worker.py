import datetime
import asyncio
import utils

from loader import bot
from workers import schedule_worker

from database.db_get import get_all_users


async def daily_worker():
    notified_lessons = []
    await schedule_worker.get_schedule_for_today()

    while True:
        current_hour_minute = datetime.datetime.now().strftime('%H:%M')
        if current_hour_minute == '00:00':
            await schedule_worker.get_schedule_for_today()

        for lesson in schedule_worker.schedule_for_today:
            if lesson['time'] == current_hour_minute:
                for user_data in await get_all_users():
                    if (lesson['subgroup'] == user_data['subgroup'] or lesson['subgroup'] == 0) and lesson['id'] not in notified_lessons:
                        await bot.send_message(user_data['user_id'], f'‼️ Скоро <b>почнеться</b> пара: {lesson["name"]}\n'
                                                                     f'📝 {utils.convert_lesson_type_to_str(lesson["type"])}  <a href="{lesson["link"]}">Посилання</a>\n'
                                                                     f'🕒 {lesson["time"]}\n')

        await asyncio.sleep(60)
