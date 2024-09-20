# Car_Shop
## Приложение для управления информацией об автомобилях.

## Описание

Приложение Car_Shop позволяет пользователям простматривать список всех автомобилей и комментариев к ним, <br/>
а так же создавать собственные автомобили и оставлять свои комментарии при прохождении регистрации.

## **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

Клонировать репозиторий:

```
git clone https://github.com/Paradaise1/car_shop.git
```

```
cd car_shop
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:


```
pip install -r requirements.txt

```

Перейти в папку с файлом manage.py

```
cd car_shop
```

Выполнить миграции:

```
python manage.py migrate
```

Загрузить в БД данный из файла db.json:

```
python manage.py loaddata db.json
```

Создайте суперюзера:
```
python manage.py createsuperuser
```

Запустить проект:

```
python manage.py runserver
```

По желанию перейти по адресу `http://127.0.0.1:8000/admin/`, войти в админку и создать там собсвенные объекты автомобилей/пользователей/комментариев.

---
По адресу `http://127.0.0.1:8000/` будет досутпна главная страница приложения.

---

## Эндпоинты API Car_Shop

POST /api/auth/users/ - зарегестрировать нового пользователя.
POST /api/auth/users/me/ - получить/обновить зарегестрированного пользователя.
POST /api/auth/jwt/create/ - создать JWT-токен.
POST /api/auth/jwt/refresh/ - получить новый JWT по истечении времени жизни ранее сгенерированного.

GET /api/cars/ — получение списка автомобилей.
GET /api/cars/<id>/ — получение информации о конкретном автомобиле.
POST /api/cars/ — создание нового автомобиля.
PUT /api/cars/<id>/ — обновление информации о автомобиле.
DELETE /api/cars/<id>/ — удаление автомобиля.
GET /api/cars/<id>/comments/ — получение комментариев к автомобилю.
POST /api/cars/<id>/comments/ — добавление нового комментария к автомобилю.

## Примеры запросов и ответов:

*Регистрация:*
**POST**```/api/auth/users/```
```
{
    "username": "string",
    "password": "string"
}
```
Ответ:
```
{
    "email": "string",
    "username": "string",
    "id": "int"
}
```

*Создать JWT токен:*
**POST**```/api/auth/jwt/create/```
```
{
    "username": "string",
    "password": "string"
}
```
Ответ:
```
{
    "refresh": "string",
    "access": "string"
}
```

*Ключевое слово для передачи JWT-токена - Bearer*

*Создать автомобиль:*
**POST**```/api/cars/```
```
{
    "make": "string",
    "model": "string",
    "year": "int",
    "description": "string"
}
```
Ответ:
```
{
    "id": "int",
    "owner": "string",
    "make": "string",
    "model": "string",
    "year": "int",
    "description": "string"
}
```

*Создать комментарий:*
**POST**```/api/comments/```
```
{
    "content": "string",
}
```
Ответ:
```
{
    "id": "int",
    "author": "string",
    "car": "string",
    "content": "string"
}
```

*Получить информацию о конкретном автомобиле:*
**GET**```/api/cars/{id}/```

Ответ:
```
{
    "id": "int",
    "owner": "string",
    "make": "string",
    "model": "string",
    "year": "int",
    "description": "string"
}
```

### Автор проекта: Роот Артём
