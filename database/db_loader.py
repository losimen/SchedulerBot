import aiosqlite


async def init_db():
    db = await aiosqlite.connect('products/database.db')

    await db.execute('CREATE TABLE IF NOT EXISTS user (' +
                        'user_id INTEGER PRIMARY KEY ,' +
                        'username TEXT NULLABLE,' +
                        'first_name TEXT NULLABLE,' +
                        'subgroup INTEGER DEFAULT 1)' )
    await db.commit()

    await db.execute('CREATE TABLE IF NOT EXISTS lesson (' +
                        'id INTEGER PRIMARY KEY AUTOINCREMENT,' +
                        'name TEXT NULLABLE,' +
                        'link TEXT NULLABLE,' +
                        'subgroup INTEGER NULLABLE,' +
                        'is_nominator INTEGER NULLABLE,' +
                        'start_time TEXT NULLABLE,'+
                        'note TEXT NULLABLE)')
    await db.commit()

    print('Database has been successfully connected')
