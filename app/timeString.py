import requests, time
from datetime import date, datetime
class timeString:
    url = 'https://yandex.ru/time/sync.json?geo=1091'

    response = requests.get(url)
    data = response.json()

    days = {
        'Mon': 'Понедельник', 'Tue': 'Вторник', 'Wed': 'Среда', 'Thu': 'Четверг', 'Fri': 'Пятница', 'Sat': 'Суббота',
        'Sun': 'Воскресенье'
    }

    month = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
        '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
    }

    zero = {
        '01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9'
    }
    def searchDay(values, searchFor):
        for k in values:
            if searchFor in k:
                return values[k]
        return None

    def searchMonth(values, searchFor):
        for k in values:
            if searchFor in k:
                return values[k]
        return None

    def searchZero(values, searchFor):
        for k in values:
            if searchFor[0:2] in k:
                return values[k] + searchFor[2:]
        return searchFor

    offsetsec = data['time'] / 1000 + (data['clocks']['1091']['offset'] / 1000 / 5 * 2)  # отступ в секундах
    realtime = datetime.fromtimestamp(offsetsec, tz=None)  # точная дата и время
    format_string = '%H:%M %m-%d'
    formatDate = datetime.strftime(realtime, format_string)  # Отформатированная строка по шаблону
    forDay = time.asctime((time.gmtime(offsetsec)))  # чтобы вычленить нужный день недели

    curTime = formatDate[0:5]  # Вывод времени
    curDay = searchDay(days, forDay[0:3])
    curMonth = ' '.join([formatDate[9:], searchMonth(month, formatDate[6:8])])
    curMonth = searchZero(zero, curMonth)
    def getString(curDay, curMonth):
        return ', '.join([curDay, curMonth])