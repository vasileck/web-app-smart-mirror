from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():

    url = 'https://yandex.ru/time/sync.json?geo=1091'

    response = requests.get(url)
    data = response.json()

    weather = {
        'city': data['clocks']['1091']['name'],
        'temperature': data['clocks']['1091']['weather']['temp'],
        'icon': data['clocks']['1091']['weather']['icon'],
        'sunrise': data['clocks']['1091']['sunrise'],
        'sunset': data['clocks']['1091']['sunset']
    }

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)