# Introduction 
...

# Build
create virtual environment
```
python -m venv venv
```
Then activate that environment
```
Windows: venv\Scripts\activate
Linux/MacOs: source venv/bin/activate
```
Then install Django in that environment
```
pip install -r requirements.txt
```
Then migrate the database
```
python manage.py migrate
```
Then create a superuser
```
python manage.py createsuperuser
```
Then run the server
```
python manage.py runserver
```
Then go to the browser and type
```
http://localhost:8000/
```
