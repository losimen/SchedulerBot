import aiosqlite
from config import DB_PATH

async def update_user_group(user_id, subgroup):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('UPDATE user SET subgroup = ? WHERE user_id = ?', (subgroup, user_id))
        await db.commit()

async def update_user_notifications(message, is_notify):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('UPDATE user SET is_notify = ? WHERE user_id = ?', (is_notify, message.chat.id))
        await db.commit()