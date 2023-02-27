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
