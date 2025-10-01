# jan25-t1b4w1-intro-to-flask
Intro to Flask and API basics

# Setup Steps

## Monday 

1. Make a venv with the command: `python3 -m venv venv`
2. Activate the venv.
	- Linux & Mac: `source venv/bin/activate`
	- Windows: `.\venv\Scripts\Activate`
3. Install Flask with `pip install flask`
4. Install `python-dotenv` with `pip install python-dotenv`
5. Preserve our packages into a requirements file with: `pip freeze > requirements.txt`
6. Make a `.env` file in the root of the repo. 
7. Make an `app.py` file in the root of the repo.
8. Copy this code into the `app.py` file: 

```python
from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

```

9. Run the server with `flask run` in the terminal.

10. Move the `app.py` file into a `src` directory, make the directory if you have to!

11. Go to our `.env` file and add `FLASK_APP=src/app.py` to the file.

12. To enable hot reloading, enable debug mode. Add this to the `.env` file: `FLASK_DEBUG=1`

## Wednesday: 

0. Add `__init__.py` to the `src` folder to make imports easier across our project as it grows.

1. Open a PostgreSQL shell by running `psql -U postgres` in your terminal.

2. Create a database for the project in the PostgreSQL shell by running `CREATE DATABASE mvc_project_db;`

3. Create a project-specific PostgreSQL user in the shell by running `CREATE USER orm_user WITH PASSWORD 'password';` in the PostgreSQL shell.


4. Modify the new user so that it has permissions to be in charge of the project database by running this in the PostgreSQL shell too: `GRANT ALL PRIVILEGES ON DATABASE mvc_project_db TO orm_user;`

5. Modify the user to give it additional permissions for the project database to allow it to modify the database design by running this in the PostgreSQL shell: `GRANT ALL ON SCHEMA public TO orm_user;`

6. Modify the database so that its owner is now the new user: `ALTER DATABASE mvc_project_db OWNER TO orm_user;`

`# DATABASE_URI=database+driver://username:password@server:port/databasename`


7. Add an ORM to our Flask project! Install some needed packages with this command in your regular terminal (no more PostgreSQL shell!): `pip install psycopg2-binary flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy`

8. Update your project's `requirements.txt` file by running `pip freeze > requirements.txt`

9. Add our new database connection string to the `.env` file with an SQLAlchemy-related key: `SQLALCHEMY_DATABASE_URI=postgresql://orm_user:password@localhost/mvc_project_db`

10. Declare some models! User first (because it has no foreign keys), then Article (because it refers to a User). Syntax may be different to the Ed content and not be impacted by the order of which models you make first - but it's a good habit to do them in an order like that in preparation for using other DB systems.

11. Declare some schemas! These give us a way to nicely go from the database to a JSON response in our API. Schemas are based on models, here.

12. Declarer some controller blueprints to use our models and schemas in the API! 

13. Register the blueprints into the `app.py` file to ensure that the API actually uses those nifty API endpoints/routes.

14. Create some CLI commands by making another blueprint, and register that into the `app.py` file as well.

15. Use the CLI commands to drop, create, and seed the database. Commands should be stuff like `flask db drop` and `flask db create` and `flask db seed`.

# Fun Helper Commands

## Postgres Shell Commands 

`\du` to list all users in our database installation.

`\l` to list all databases in our database installation.

## Flask CLI Commands 

Use `flask run