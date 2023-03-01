import aiosqlite
from config import DB_PATH

async def get_user(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT * FROM user WHERE user_id = ?', (user_id,)) as cursor:
            user = await cursor.fetchone()

            if user is None:
                return None

            user_result = {
                'user_id': user[0],
                'username': user[1],
                'first_name': user[2],
                'subgroup': user[3],
                'is_notify': user[4],
                'is_admin': user[5]
            }

            return user_result


async def get_schedule_for_weekday(weekday: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT * FROM lesson WHERE weekday = ?', (weekday,)) as cursor:
            schedule = await cursor.fetchall()

            if schedule is None:
                return None

            schedule_result = []

            for lesson in schedule:
                lesson_result = {
                    'id': lesson[0],
                    'name': lesson[1],
                    'link': lesson[2],
                    'subgroup': lesson[3],
                    'is_nominator': lesson[4],
                    'teacher': lesson[5],
                    'type': lesson[6],
                    'note': lesson[7],
                    'weekday': lesson[8],
                    'time': lesson[9]
                }

                schedule_result.append(lesson_result)

            return schedule_result


async def get_all_users():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT * FROM user') as cursor:
            users = await cursor.fetchall()

            if users is None:
                return None

            users_result = []

            for user in users:
                user_result = {
                    'user_id': user[0],
                    'username': user[1],
                    'first_name': user[2],
                    'subgroup': user[3],
                    'is_notify': user[4],
                    'is_admin': user[5]
                }

                users_result.append(user_result)

            return users_result