import aiosqlite


async def init_db():
    db = await aiosqlite.connect('products/database.db')

    await db.execute('CREATE TABLE IF NOT EXISTS user (' +
                        'user_id INTEGER PRIMARY KEY ,' +
                        'username TEXT NULLABLE,' +
                        'first_name TEXT NULLABLE,' +
                        'subgroup INTEGER DEFAULT 1,' +
                        'is_notify INTEGER DEFAULT 1,'
                        'is_admin INTEGER DEFAULT 0)')
    await db.commit()


    # lesson_name, lesson_link,
    # lesson_subgroup, lesson_is_nominator,
    # lesson_teacher, lesson_type,
    # lesson_note, lesson_start

    await db.execute('CREATE TABLE IF NOT EXISTS lesson (' +
                        'id INTEGER PRIMARY KEY AUTOINCREMENT,' +
                        'name TEXT NULLABLE,' +
                        'link TEXT NULLABLE,' +
                        'subgroup INTEGER NULLABLE,' +
                        'is_nominator INTEGER NULLABLE,' +
                        'teacher TEXT NULLABLE,' +
                        'type INTEGER NULLABLE,' +
                        'note TEXT NULLABLE,' +
                        'weekday INTEGER NULLABLE,'
                        'time TEXT NULLABLE)')
    await db.commit()

    print('Database has been successfully connected')
