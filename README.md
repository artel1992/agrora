### Создание окружения
```console
python -m pip install pipenv or
python -m pip install --user virtualenv
python -m venv venv
```

### Запуск проекта
```console
pipenv shell or .\venv\Scripts\activate
pipenv install or pip install -r .\requirements.txt
cd .\front
npm i
cd ..
pipenv run migrations or python manage.py makemigrations
pipenv run migrate or python manage.py migrate
```