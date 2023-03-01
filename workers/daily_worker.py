import datetime
import asyncio
import utils

from loader import bot
from workers import schedule_worker

from database.db_get import get_all_users


# check whether hour and minute are less than 10 and add 0 to the beginning
def has_time_range(time_1, time_2, minute_range):
    time_1 = datetime.datetime.strptime(time_1, '%H:%M')
    time_2 = datetime.datetime.strptime(time_2, '%H:%M')
    time_2 = time_2 + datetime.timedelta(minutes=minute_range)

    return time_1 <= time_2



async def daily_worker():
    notified_lessons = []
    await schedule_worker.get_schedule_for_today()

    while True:
        current_hour_minute = datetime.datetime.now().strftime('%H:%M')
        if current_hour_minute == '00:00':
            await schedule_worker.get_schedule_for_today()

        for lesson in schedule_worker.schedule_for_today:
            if has_time_range(current_hour_minute, lesson['time'], 30):
                for user_data in await get_all_users():
                    if (lesson['subgroup'] == user_data['subgroup'] or lesson['subgroup'] == 0) and lesson['id'] not in notified_lessons:
                        await bot.send_message(user_data['user_id'], f'‼️ Скоро <b>почнеться</b> пара: {lesson["name"]}\n'
                                                                     f'📝 {utils.convert_lesson_type_to_str(lesson["type"])}  <a href="{lesson["link"]}">Посилання</a>\n'
                                                                     f'🕒 {lesson["time"]}\n')
                        notified_lessons.append(lesson['id'])

        await asyncio.sleep(60)
