from flask import Flask, render_template, jsonify
from timeString import timeString
import requests
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Таблица списка покупок
class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Purchases {self.item_name}>"

#Таблица списка дел
class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(255), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<ToDoList {self.task_name}>"

#Основная страница, где отображается город, время и погода
@app.route('/')
def index():
    purchases = Purchases.query.all()
    todolist = ToDoList.query.all()
    weather = {
        'city': timeString.data['clocks']['1091']['name'],
        'temperature': timeString.data['clocks']['1091']['weather']['temp']
    }
    return render_template('index.html', weather=weather, purchases=purchases, todolist=todolist)

#Обновление температуры
@app.route('/get_temperature')
def get_temperature():
    url = os.getenv('WEATHER_URL')

    response = requests.get(url)
    data = response.json()
    temperature = data['clocks']['1091']['weather']['temp']
    return jsonify({'temp': temperature})

#Апдейт статуса для списка покупок
@app.route('/update/<int:id>', methods=['POST'])
def update_status(id):
    purchase = Purchases.query.get_or_404(id)
    purchase.active = not purchase.active
    db.session.commit()

    return jsonify({'active': purchase.active})

#Апдейт статуса для списка дел
@app.route('/updatetodo/<int:id>', methods=['POST'])
def update_statustodo(id):
    task = ToDoList.query.get_or_404(id)
    task.is_completed = not task.is_completed
    db.session.commit()
    return jsonify({'is_completed': task.is_completed})

#Удалить в списке покупок
@app.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    item_to_delete = Purchases.query.get_or_404(id)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return jsonify({'success': True})
    except:
        db.session.rollback()
        return jsonify({'success': False}), 500

#Удалить в списке дел
@app.route('/deletetodo/<int:id>', methods=['POST'])
def delete_itemtodo(id):
    # Получаем запись по её ID
    item_to_delete = ToDoList.query.get_or_404(id)

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