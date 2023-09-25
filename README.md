# picasso_test_project
Test project for vacation Picasso
Сервис разработан на Django Rest Framework с Celery/Redis
## Установка и запуск


1. Склонировать репозиторий с Github
2. Перейти в директорию проекта
3. Создать файл .env заполнить в нем поля
```
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DJANGO_SETTINGS_MODULE=freight.settings
DATABASE_URL=
```
4. Запустить контейнеры
```
sudo docker-compose up -d
```
5. Остановка работы контейнеров
```
sudo docker-compose stop
```
***
```http://0.0.0.0:8000/files/```  - Принимает post, get, delete запросы.