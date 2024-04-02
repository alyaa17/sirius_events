import tg_parser
import sirius_parser_ft
import park_sirius_parser

tg_data = tg_parser.main()
data = sirius_parser_ft.main()
data.extend(tg_data)

for elem in data:
    print(elem)
    print('_________________')

# print(park_sirius_parser.main()) # готовые данные
