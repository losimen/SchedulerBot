def convert_weekday_index_to_name(weekday_index: int):
    weekdays = {
        0: 'Понеділок',
        1: 'Вівторок',
        2: 'Середа',
        3: 'Четвер',
        4: 'П\'ятниця',
        5: 'Субота',
        6: 'Неділя'
    }

    return weekdays[weekday_index]


def convert_number_to_emoji(number: int):
    emojis = {
        0: '0️⃣',
        1: '1️⃣',
        2: '2️⃣',
        3: '3️⃣',
        4: '4️⃣',
        5: '5️⃣',
        6: '6️⃣',
        7: '7️⃣',
        8: '8️⃣',
        9: '9️⃣',
        10: '🔟'
    }

    return emojis[number]


def convert_lesson_type_to_str(lessontype: int):
    types = [
        'Лекція',
        'Практична',
        'Лабораторна'
    ]
    return types[lessontype - 1]