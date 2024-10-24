# web-app-smart-mirror

## Описание проекта
Умное зеркало — это интерактивное устройство, которое сочетает в себе функциональность традиционного зеркала и современные технологии. Оно отображает:

**Текущее время**

**Погоду в городе**

**Список дел**

**Список покупок**

Проект разработан с использованием Flask для серверной части и JavaScript для динамического обновления информации на странице.

## Функциональность

**Время**: отображение актуального времени с обновлением каждую минуту.

**Погода**: получение данных о погоде из внешнего API.

**Списки**: пользователи могут удалять задачи из списка дел и покупок, а изменения отображаются в реальном времени.

## Технологии
**Flask**: для разработки серверной логики.

**HTML/CSS**: для создания пользовательского интерфейса.

**JavaScript**: для динамического обновления информации на странице.

**MySQL**: для хранения данных о списках дел и покупок.


## Установка
Клонируйте репозиторий.

***Обязательно*** указать соединение к бд в строке app.config['SQLALCHEMY_DATABASE_URI']

Запустите сервер, например, через pycharm.

Откройте браузер и перейдите по адресу http://localhost:5000.

## Смена города

Чтобы сменить город, нужно подставить код своего города в ссылку https://yandex.ru/time/sync.json?geo=1091, в параметр geo.
Узнать код города можно через поисковую строку Яндекс, вбив в поиск запрос Погода.  Параметр lr.

![Описание изображения](https://github.com/vasileck/web-app-smart-mirror/blob/main/beEVeASA9YM.jpg)

## Вклад
Если вы хотите внести свой вклад, пожалуйста, откройте вопрос или создайте запрос на перенос (pull request).
