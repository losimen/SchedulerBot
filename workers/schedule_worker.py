import datetime

from database.db_get import get_schedule_for_weekday

schedule_for_today = []

async def get_schedule_for_today() -> list:
    global schedule_for_today

    schedule_for_today = []
    current_day = datetime.datetime.today().weekday()

    print(current_day)
    schedule_for_today = await get_schedule_for_weekday(current_day)

    return schedule_for_today
