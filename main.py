import tg_parser
import sirius_parser_ft
import park_sirius_parser

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


# print(park_sirius_parser.main()) # готовые данные

