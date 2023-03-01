import aiosqlite
from config import DB_PATH

async def insert_user(user_id, username, first_name):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('INSERT INTO user (user_id, username, first_name) VALUES (?, ?, ?)',
                         (user_id, username, first_name))
        await db.commit()


async def insert_lesson(lesson):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('INSERT INTO lesson (name, link, subgroup, is_nominator, teacher, type, weekday, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                         (lesson['name'], lesson['link'], lesson['subgroup'], lesson['is_nominator'], lesson['teacher'], lesson['type'], lesson['weekday'], lesson['time']))
        await db.commit()
