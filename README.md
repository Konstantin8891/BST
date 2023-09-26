# R4C - Robots for consumers

## Описание

 Сервис учёта и заказа произведённой продукции

## Стек

Python 3.11

Django 4.2

Xlsxwriter 3.1.5


## Инструкции по запуску

git clone https://github.com/Konstantin8891/BST.git

cd BST

python -m venv venv

Linux:

source venv/bin/activate

Windows:

source venv/Scripts/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

## Запросы к проекту

Добавление произведённого робота

POST

http://localhost:8000/robots/add_robot/

{"model":"R2","version":"D7","created":"2023-09-25 12:00:01"}

Загрузка Excel-отчёта по производству за текущую неделю

GET

http://localhost:8000/robots/weekly_report/

Добавление покупателя

POST

http://localhost:8000/customers/add_customer/

{"email": "89670253660@mail.ru"}

 Размещение заказа

 POST

 http://localhost:8000/orders/add_order/

{"customer": 1, "robot_serial": "R2-D7"}
