import requests
class timeString:
    url = 'https://yandex.ru/time/sync.json?geo=1091'


    response = requests.get(url)
    data = response.json()



