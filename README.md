# Приложение "Хранилище паролей"

### Доступа пользователя к личному хранилищу паролей осуществляется с предварительным вводом пароля.
### этот пароль можно создать, удалить и изменить.

## Используемые технологии:
- Python
- Django 
- Docker
- PostgreSQL
- Nginx

### !ВАЖНО! Для работы сервиса необходим заранее установленный Docker и docker-compose
- Клонировать репозиторий git clone https://github.com/h0diush/password_store-.git
- В корне проекта создайте файл .env и заполнить его следующими данными:
```
SECRET_KEY=django-insecure-^^&cn=v_7v#r3sx=h1blx(fim=c2#b5&s$nj+5bldio6i)nte7
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DEBUG=True

DB_ENGINE=...
DB_NAME=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
DB_HOST=...
DB_PORT=...

EMAIL_BACKEND=...
EMAIL_HOST=...
EMAIL_PORT=...
EMAIL_USE_TLS=...
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...  
 ```

- Сделайте миграции python3 manage.py makemigrations & python3 manage.py migrate
- Заполните БД тестовыми данными: python3 manage.py loaddata data/data.json
- Запуск если DEBUG = True python3 manage.py runserver
- Если DEBUG = False docker-compose up -d --build
- Для запуска тестов введите в консоли python3 manage.py test -v 2
