# Тестовое задание для ШИФТ

Данный REST-сервис продоставляет данный спект возможностей:

- Добавление сотрудника в базу данных.
- Создание уникального токена по логину и паролю сотридника.
- Получение чувствительных данных (зарбплата и дата повышения) только по валидному токену.

---

![12](https://img.shields.io/github/pipenv/locked/python-version/TriNitki/shift_zadanie?logo=python) ![12](https://img.shields.io/badge/PostgreSQL-15.2-red/?color=%23336791&logo=postgresql&logoColor=white) ![12](https://img.shields.io/badge/Docker-24.2-red/?color=%23039bc5&logo=docker) ![12](https://img.shields.io/github/pipenv/locked/dependency-version/TriNitki/shift_zadanie/fastapi?color=%2305988a&logo=fastapi)

## Установка

### Дефолтная установка

1. Клонирование репозитория.

    ```bash
    git clone https://github.com/TriNitki/tg_case_bot
    ```

2. Установка необходимых пакетов.

    - Poetry

        ```shell
        poetry install
        ```

    - PIP

        ```shell
        pip install -r requirements.txt
        ```

3. Добавление переменных окружения

    ```py
    # ./app/config.py

    # Вставьте данные для подключения к базе данных
    db_user = '' # Postgres data base user
    db_pass = '' # Postgres data base password
    db_port = '' # Postgres data base port
    db_name = '' # Postgres data base name
    ```


### Установка для Docker
