# Bake cake

Площадка для приёма заказов на торты

## Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно указать их в файле `./application/config/.env` 
Передача значений ПеО происходит с использованием [python-dotenv](https://pypi.org/project/python-dotenv/).

### Параметры проекта

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`BOT_API_TOKEN`| Токен Telegram-бота | - |
|`ALLOWED_HOSTS`| Разрешённые хосты |`['0.0.0.0', '127.0.0.1', 'localhost']`|
|`DEBUG`| Режим отладки |`False`|
|`SECRET_KEY`| Уникальное непредсказуемое значение |-|


### Параметры подключения к БД

По умолчанию, используется СУБД PostgreSQL.

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DB_ENGINE`| Имя движка СУБД | - |
|`DB_HOST`| Адрес СУБД | `127.0.0.1` |
|`DB_PORT`| Порт СУБД | - |
|`DB_NAME`| Имя БД | - |
|`DB_USER`| Имя пользователя БД | `postgres` |
|`DB_PASSWORD`| Пароль пользователя БД | - |

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

- установить и настроить Docker,
- установить и настроить Redis,
- скорректировать ./Docker/init_user_and_db.sql  # подсказки внутри
- собрать образ для создания контейнера с PostgreSQL,
- запустить контейнер в режиме демона:
```sh
docker-compose build
docker-compose up -d
```

- создать миграцию,
- применить миграцию к проекту:
```sh
python manage.py makemigrations
python manage.py migrate
```

- создать суперпользователя в интерактивном режиме**,
- запустить бота и админку,
- перейти на [сайт](http://127.0.0.1:8000/admin/) для наполнения БД.
```bash
python manage.py createsuperuser
python app.py
```



\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

\** для наполнения БД через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
