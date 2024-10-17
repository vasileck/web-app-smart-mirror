from flask import Flask, render_template, jsonify, redirect, request
from timeString import timeString
import requests
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u1634956_nastya:Nastya1_Nastya2@smart-tech.su/u1634956_nastya'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Purchases {self.item_name}>"

@app.route('/')
def index():
    purchases = Purchases.query.all()
    show_form = False
    weather = {
        'city': timeString.data['clocks']['1091']['name'],
        'temperature': timeString.data['clocks']['1091']['weather']['temp']
    }
    return render_template('index.html', weather=weather, purchases=purchases, show_form=show_form)


@app.route('/get_temperature')
def get_temperature():
    url = 'https://yandex.ru/time/sync.json?geo=1091'

    response = requests.get(url)
    data = response.json()
    temperature = data['clocks']['1091']['weather']['temp']
    return jsonify({'temp': temperature})


@app.route('/update/<int:id>', methods=['POST'])
def update_status(id):
    # Найдем продукт по его id
    purchase = Purchases.query.get_or_404(id)
    # Изменим статус active на противоположный
    purchase.active = not purchase.active
    # Сохраним изменения в базе данных
    db.session.commit()

    # Возвращаем ответ с текущим статусом
    return jsonify({'active': purchase.active})


@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    quantity = request.form['quantity']

    # Создаем новую запись
    new_item = Purchases(item_name=item_name, quantity=quantity)

    # Добавляем в базу данных
    db.session.add(new_item)
    db.session.commit()

    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    # Получаем запись по её ID
    item_to_delete = Purchases.query.get_or_404(id)

    try:
        # Удаляем запись из базы данных
        db.session.delete(item_to_delete)
        db.session.commit()
        return jsonify({'success': True})
    except:
        db.session.rollback()
        return jsonify({'success': False}), 500

if __name__ == '__main__':
    app.run(debug=True)