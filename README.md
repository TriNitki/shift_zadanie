# Тестовое задание для ШИФТ

Данный REST-сервис продоставляет данный спект возможностей:

- Добавление сотрудника в базу данных.
- Создание уникального токена по логину и паролю сотрудника.
- Получение чувствительных данных (зарплата и дата повышения) только по валидному токену.

##

![12](https://img.shields.io/github/pipenv/locked/python-version/TriNitki/shift_zadanie?logo=python) ![12](https://img.shields.io/badge/PostgreSQL-15.2-red/?color=%23336791&logo=postgresql&logoColor=white) ![12](https://img.shields.io/badge/Docker-24.2-red/?color=%23039bc5&logo=docker) ![12](https://img.shields.io/github/pipenv/locked/dependency-version/TriNitki/shift_zadanie/fastapi?color=%2305988a&logo=fastapi)

## Взаимодействие с проектом

Сперва, установите проект при помощи одного из нижеперечисленных методов установки. Затем, для взаимодействия вам потребуется перейти <http://localhost:8000/docs/> или <http://localhost:8008/docs/> (в зависимости от выбранного вами метода работы проекта). Перейдя по одной из указанных ранее ссылок, откроется документация Swagger, которая вам поможет разобраться с функционалом сервиса.

## Установка

Клонирование репозитория

```bash
$ git clone https://github.com/TriNitki/shift_zadanie
```

### Локальная установка

1. Установка необходимых пакетов

    - Poetry

        ```shell
        $ poetry install
        ```

    - PIP

        ```shell
        $ pip install -r requirements.txt
        ```

2. Добавление переменных окружения в [config](/app/config.py)

    ```py
    # ./app/config.py

    # Вставьте данные для подключения к базе данных
    db_user = '' # Postgres data base user
    db_pass = '' # Postgres data base password
    db_port = '' # Postgres data base port
    db_name = '' # Postgres data base name
    ```

3. Запуск

    ```shell
    $ uvicorn app.main:app
    ```

После установки перейдите по ссылке <http://127.0.0.1:8000> и вы увидите главную страницу.

### Установка для Docker

1. Добавление переменных окружения в [docker-compose](/docker-compose.yml)

   ```docker
    # ./docker-compose.yml

    services:
      web:
        ...
        environment:
          - DATABASE_URL=postgresql://<user>:<password>@db:5432/<db> # insert db info
        ...
      db:
        ...
        environment: # insert db info
          - POSTGRES_USER=<user>
          - POSTGRES_PASSWORD=<password>
          - POSTGRES_DB=<db>
   ```

2. Сборка образа

    ```shell
    $ docker-compose build
    ```

3. Запуск и активация контейнера

    ```shell
    $ docker-compose up -d --build
    ```

После установки перейдите по ссылке <http://localhost:8008/> и вы увидите главную страницу.


