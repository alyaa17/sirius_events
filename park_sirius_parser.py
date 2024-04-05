import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from sirius_parser_ft import remove_html_tags

site_link = 'https://parksirius.ru'
links = set()


def main():
    response = requests.get(site_link)
    soup = BeautifulSoup(response.text, "html.parser")
    for event in soup.find_all('div', class_='list-item'):
        # событие
        event_desc = event.find('div', class_='col-lg-10 col-md-9 col-sm-12 col-xs-12')
        event_title = event_desc.find('h2')
        event_title = remove_html_tags(str(event_title))

        # получение места события
        location_event = event.find('span', class_='stats')
        location_event = remove_html_tags(str(location_event))

        # получение даты события
        event_date = event.find('span', class_='ticket-buy dimbox-grey')
        event_date = remove_html_tags(str(event_date))

        text_desc = remove_html_tags(str(event_desc))
        text_desc = text_desc.strip()
        lines = text_desc.split('\n')
        key_for_date = ['Время', 'Сеанс', 'Начало']
        for line in lines:
            for key in key_for_date:
                if key in line:
                    time = line.split(':', maxsplit=1)[1]
                    time = time.strip()
                    event_date += f' - {time}'

        # получение стоимости
        event_price = 'Нет данных о стоимости посещения'
        link = event_desc.find('a').get('href')
        link = remove_html_tags(str(link))
        link = f'https://parksirius.ru{link}'
        try:
            response = requests.get(link)
            full_desc_event = (BeautifulSoup(response.text, 'html.parser')
                               .find('div', class_='col-xs-12 event-details-content'))
            key_for_price = ['Стоимость', 'Цена', 'Билеты']
            for p in full_desc_event.find_all('p'):
                line = remove_html_tags(str(p))
                for key in key_for_price:
                    if key in line:
                        if '\n' not in line:
                            event_price = line
                        else:
                            phrases = line.split('Стоимость', maxsplit=1)[1]
                            phrase = phrases.split('.', maxsplit=1)[0]
                            event_price = 'Стоимость' + phrase + '.'
        except:
            with open('garbage.txt', 'w') as file:
                file.write(link)
        print(event_title, location_event, event_date, event_price, link, sep='\n')
        print('__________________')

    return 0


if __name__ == '__main__':
    main()
