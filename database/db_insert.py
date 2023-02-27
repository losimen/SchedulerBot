import aiosqlite
from config import DB_PATH

async def insert_user(user_id, username, first_name):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('INSERT INTO user (user_id, username, first_name) VALUES (?, ?, ?)',
                         (user_id, username, first_name))
        await db.commit()