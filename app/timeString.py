import requests
from dotenv import load_dotenv
import os

load_dotenv()
class timeString:
    url = os.getenv('WEATHER_URL')


    response = requests.get(url)
    data = response.json()



