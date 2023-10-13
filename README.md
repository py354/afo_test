## Запуск
1. Создать в postgres базу данных для приложения, например afo_test:
```console
$ createdb afo_test
```
2. Записать данные для подключения в файл .env
3. Установить зависимости:
```console
$ pip install -r requirements.txt
```
4. Выполнить инициализацию и миграцию бд:
```console
$ flask db init 
$ flask db migrate 
$ flask db upgrade
```
Приложение запускается с помощью flask cli:
```console
$ flask run
```
Например, установка порта и хоста:
```console
$ flask run -h 0.0.0.0 -p 5000
```
Перед запуском необходимо настроить Postgres, создать базу данных и указать параметры подключения в файле .env

## Запуск с Docker
1. Создать в postgres базу данных для приложения, например afo_test:
```console
$ createdb afo_test
```
2. Записать данные для подключения в файл .env
3. Создать и запустить контейнер
```console
$ docker build --rm -t afo_test .
$ docker run --network="host" afo_test
```

## Переменные
Настройки среды установлены в файле .env:
```
DB_HOST=localhost
DB_PORT=5432
DB_USER=danis
DB_PASS=danis
DB_NAME=afo_test
SECRET_KEY="7f58560c66865cbc5ea4eb4aa11d9ec1bc005a82"
```