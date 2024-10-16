from flask import Flask, render_template, jsonify
from timeString import timeString
import requests



app = Flask(__name__)

@app.route('/')
def index():

    weather = {
        'city': timeString.data['clocks']['1091']['name'],
        'temperature': timeString.data['clocks']['1091']['weather']['temp'],
        'sunrise': timeString.data['clocks']['1091']['sunrise'],
        'sunset': timeString.data['clocks']['1091']['sunset'],
    }
    return render_template('index.html', weather=weather)


@app.route('/get_temperature')
def get_temperature():
    url = 'https://yandex.ru/time/sync.json?geo=1091'

    response = requests.get(url)
    data = response.json()
    temperature = data['clocks']['1091']['weather']['temp']
    return jsonify({'temp': temperature})

if __name__ == '__main__':
    app.run(debug=True)