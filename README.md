# Bake cake

Площадка для приёма заказов на торты

## Описание

Telegram-бот для сборки и заказа тортов

### Начало работы

* Получить токен у [@BotFather](https://t.me/botfather)

### Особенности

* позволяет собрать торт из предоставляемых на выбор [ингредиентов](https://github.com/Padking/bake-cake/wiki#Понятия),
* предоставляет возможность инициировать заказ,
* обеспечивает регистрацию Пользователя (П) до/после процедуры сбора торта.

## Примеры использования

  Регистрация:

  ![bot_1_registration](https://github.com/Padking/bake-cake/blob/master/screenshots/bot_1_registration.png)


  Сборка торта:

  ![bot_2_create_cake](https://github.com/Padking/bake-cake/blob/master/screenshots/bot_2_create_cake.png)


## Структура проекта

### ПО [бота](https://github.com/Padking/bake-cake/tree/master/application/apps/core/bot)
- набор [обработчиков](https://github.com/Padking/bake-cake/tree/master/application/apps/core/bot/handlers) запросов П-ля,
- набор вспомогательных [функций](https://github.com/Padking/bake-cake/tree/master/application/apps/core/bot/helpers).

### Используемые технологии

* [aiogram](https://docs.aiogram.dev/en/latest/index.html)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Redis](https://redis.io/)
* [Tortoise ORM](https://tortoise.github.io/toc.html)
* [uvicorn](https://www.uvicorn.org/)

## Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно указать их в файле `./application/config/.env` 
Передача значений ПеО происходит с использованием [python-dotenv](https://pypi.org/project/python-dotenv/) и [environs](https://pypi.org/project/environs/).

### Параметры проекта

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`BOT_API_TOKEN`| Токен Telegram-бота | - |
|`CONSENT_PD_FILEPATH`| Абсолютный путь к [СОПД](https://github.com/Padking/bake-cake/wiki#Понятия) | - |
|`HELP_PHOTO_FILEPATH`| Абсолютный путь к [отбивке](https://github.com/Padking/bake-cake/wiki#Понятия) | - |
|`ALLOWED_HOSTS`| Разрешённые хосты |`['0.0.0.0', '127.0.0.1', 'localhost']`|
|`DEBUG`| Режим отладки |`False`|
|`SECRET_KEY`| Уникальное непредсказуемое значение |-|


### Параметры подключения к БД

Используются СУБД PostgreSQL и Redis.

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DB_ENGINE`| Имя движка СУБД | - |
|`DB_HOST`| Адрес СУБД | `127.0.0.1` |
|`DB_PORT`| Порт СУБД | - |
|`DB_NAME`| Имя БД | - |
|`DB_USER`| Имя пользователя БД | `postgres` |
|`DB_PASSWORD`| Пароль пользователя БД | - |
|`REDIS_HOST`| Адрес СУБД | `127.0.0.1` |
|`REDIS_PORT`| Порт СУБД | - |
|`REDIS_DB_PASSWORD`| Пароль пользователя БД | - |

## Установка

- клонировать проект,
- создать каталог виртуального окружения (ВО)*,
- связать каталоги ВО и проекта,
- установить зависимости:
```sh
git clone https://github.com/Padking/bake-cake.git
cd bake-cake
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt
```

- применить миграцию к проекту:
```sh
python manage.py migrate
```

- запустить бота,
```bash
python app.py
```



\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
