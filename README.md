https://github.com/loverazz/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg

# Yamdb API

### Yamdb - reviews resource

##### Description

The YaMDb project collects reviews (Review) of users on works (Titles). The works are divided into categories: "Books", "Films", "Music". The list of categories (Category) can be expanded by the administrator (for example, you can add the category "Fine Arts" or "Jewellery").


##### Technologies

- Python 3.7
- Django 2.2.19
- Django REST framework


##### .env file template

```
# in project_directory/project_name/project_name/.env
# specify the database - postgresql
DB_ENGINE=django.db.backends.postgresql
# specify database name
DB_NAME=yatube
# specify username
POSTGRES_USER=yatube_user
# specify password
POSTGRES_PASSWORD=xxxyyyzzz
# specify localhost
DB_HOST=127.0.0.1
# specify post for connection to database
DB_PORT=5432
```


##### Build the container

```
docker-compose up -d --build 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```


##### Authors

1. Auth/Users - Kseniia Nivnia
2. Categories/Genres/Titles - Elina Anastasia
3. Review/Comments - Kashtanov Nikolai

Moscow, 2022
