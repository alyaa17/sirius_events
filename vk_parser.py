import requests
from datetime import datetime


token = '878b68a8878b68a8878b68a873849ca4b68878b878b68a8e18db916d0b1536fcb7c4b6a'
# https://api.vk.com/method/wall.get?access_token=878b68a8878b68a8878b68a873849ca4b68878b878b68a8e18db916d0b1536fcb7c4b6a&v=5.13&domain=sirius.afisha
version = 5.82
domain = 'sirius.afisha'

response = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'domain': domain,
                            'count': 10
                        })

data = response.json()['response']['items']

for post in data:
    current_dt = datetime.now()
    timestamp = post['date']
    dt_object = datetime.fromtimestamp(timestamp)
    time_diff = current_dt - dt_object
    if time_diff.total_seconds() < 24 * 3600:
        print(post['text'])
