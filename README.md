## Запуск
Приложение запускается с помощью cli flask:
```console
$ flask run
```
Например, установка порта и хоста:
```console
$ flask run -h 0.0.0.0 -p 5000
```
Перед запуском необходимо настроить Postgres, создать базу данных и указать параметры подключения в файле .env 

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

