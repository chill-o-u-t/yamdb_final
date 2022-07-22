# Yamdb with Docker and workflows
## База отзывов пользователей о фильмах, музыке и книгах
## Стек технологий: Python 3, Django REST Framework, PostgreSQL, Simple-JWT, NGINX, Docker, flake, pytest
### Статус workflow: 
![example workflow](https://github.com/chill-o-u-t/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
____
##### Создание файла с переменными окружения .env
Пример:
- выбор движка СУБД ```DB_ENGINE=django.db.backends.postgresql```
- название базы ```DB_NAME=postgres```
- имя пользователя базы ```POSTGRES_USER=postgres```
- пароль базы данных ```POSTGRES_PASSWORD=postgres```
- адрес базы ```DB_HOST=db``` 
- порт базы```DB_PORT=5432```


### Запуск приложения:
```docker-compose up```

### Выполнить миграции:
```docker-compose exec web python manage.py makemigrations``` \
```docker-compose exec web python manage.py migrate``` 

### Создать суперпользователя для windows :
```winpty docker-compose exec web python manage.py createsuperuser```

## Тестовая база данных
Создание тестовой базы данных осуществляется с помощью файла управления Django-проектом:
```
api_yamdb\manage.py
```
Файл скрипта располагается в следующем каталоге:
```
api_yamdb\reviews\management\commands\fill_db.py
```
Что бы создать тестовую базу нужно выполнить команду:
```
python3 manage.py fill_db
```

### Проект доступен по адресу:
http://84.201.155.122:5000

### Информация об образе на Dockerhub
```chil1out/yamdb```
### Информация об авторе проекта
```Ivan Morozov```


