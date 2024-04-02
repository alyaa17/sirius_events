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
    for a in soup.find_all('a'):
        href_link = a.get('href')
        if '/event' in href_link:
            links.add(f'https://parksirius.ru{href_link}')
    for link in links:
        try:
            response = requests.get(link)
            event = BeautifulSoup(response.text, "html.parser")
            text_event = str(event.find_all(['b', 'br', 'p', 'h1', 'span']))
            text_event = remove_html_tags(text_event)
            print(text_event[1:-1])
            # date_event
            print('------------------------------')
        except:
            pass
    return 0


if __name__ == '__main__':
    main()
