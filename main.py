import tg_parser
import sirius_parser_ft
import park_sirius_parser
import sqlite3

words_in_events = ['фестиваль', 'состоится', 'мероприятие', 'концерт', 'билеты', 'выходные', 'соревнование']


def check_event(event):
    for word in words_in_events:
        if word.lower() in event:
            return 1
    return 0


tg_data = tg_parser.main()
data = sirius_parser_ft.main()
data.extend(tg_data)

data = park_sirius_parser.main()

# подключение к бд
db = sqlite3.connect('upcoming_events.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        event TEXT,
        date TIMESTAMP,
        location TEXT,
        price TEXT ) ''')

data_to_insert = list()
for ev in data:
    ev_information = (ev[0], ev[2], ev[1], ev[3])
    data_to_insert.append(tuple(ev_information))

with open('text', 'w') as file:
    file.write('an')

for elem in data_to_insert:
    q = f"SELECT id FROM events WHERE event = '{elem[0]}' AND date = '{elem[1]}'"
    cursor.execute(q)
    existing_ev= cursor.fetchone()
    if not existing_ev:
        cursor.execute(f"INSERT INTO events (event, date, location, price) VALUES (?, ?, ?, ?)", elem)

db.commit()
db.close()
