from flask import Flask, render_template
import requests
from timeString import timeString

app = Flask(__name__)

@app.route('/')
def index():

    curTime = timeString.curTime
    curDay = timeString.getString(timeString.curDay, timeString.curMonth)

    weather = {
        'city': timeString.data['clocks']['1091']['name'],
        'temperature': timeString.data['clocks']['1091']['weather']['temp'],
        'icon': timeString.data['clocks']['1091']['weather']['icon'],
        'sunrise': timeString.data['clocks']['1091']['sunrise'],
        'sunset': timeString.data['clocks']['1091']['sunset'],
        'time': curTime,
        'day': curDay
    }

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)