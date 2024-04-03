import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


link = 'https://sirius-ft.ru/news'
data = []

def remove_html_tags(text):
    cleaned_text = re.sub(r'<[^>]*>,?', '', text)
    return cleaned_text


def main():
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    count = 0
    for href_link in soup.find_all('a'):
        if 37 < count < 45:
            res_link = href_link.get('href')
            if len(res_link) > 2:
                response = requests.get(f'https://sirius-ft.ru{res_link}')
                post = BeautifulSoup(response.text, "html.parser")

                text_inf = str(post.find_all(['b', 'br', 'p', 'h1', 'span']))
                clean_text_inf = remove_html_tags(text_inf[1:-1])

                text_post = str(post.find_all(['div'], class_='t-redactor__tte-view'))
                clean_text_post = remove_html_tags(text_post[1:-1])

                text_join = clean_text_inf[588:-1005] + clean_text_post

                date = re.search(r'\d{2}.\d{2}.\d{4}', clean_text_inf).group()
                date = date.replace('.', '-')

                date_now = str(datetime.now()).split(' ')[0].split('-')[::-1]
                date_now = '-'.join(date_now)

                if date == date_now and text_join:
                    data.append(text_join)
        count += 1

    return data


if __name__ == '__main__':
    main()
