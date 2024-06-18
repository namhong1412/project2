# Run BE project

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

- Run the queries in the `example.sql` file in the BE directory

```
python manage.py makemigrations
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

## Run FE project

**Prerequisites:**

* Node.js v18 and npm (or yarn) installed on your system.

**Steps:**

1. **Navigate to the project directory:**
   ```bash
   cd FE
   ```

2. **Install dependencies:**
   ```bash
    npm install
    ```
   or
    ```bash
    yarn install
    ```
3. **Start the development server:**
    ```bash
    npm run dev
    ```
4. **Access your application:**
   Open `http://localhost:3000` in your web browser.

5. **Build the project:**
    ```bash
    npm run build
    ```
   or
    ```bash
    yarn build
    ```
