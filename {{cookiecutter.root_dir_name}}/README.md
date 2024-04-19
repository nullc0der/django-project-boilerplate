### How to run the project

```bash
    cp sample.env .env
```

Fill the .env file

Install python poetry and dotenv

```bash
    dotenv run poetry run python manage.py migrate
    dotenv run poetry run python manage.py createsuperuser
    dotenv run poetry run python manage.py runserver
```
