import os # built-in Python module
from flask import Flask, jsonify # pip install Flask
from dotenv import load_dotenv # pip install python-dotenv
from src.init import db  # our database object from init.py
from src.controllers.cli_controller import db_commands
from src.controllers.user_controller import user_bp

load_dotenv()  # take environment variables from .env.

def create_app():
    app = Flask(__name__)
    print("Flask server starting up...")

    # set the database URI via SQLAlchemy, 
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    # keep jsonified data in same order as we wrote it
    app.json.sort_keys = False  

    #create the database object
    db.init_app(app)


    @app.route("/")
    def hello_world():
        return "<p>Hello, pizza!</p>"
    
    # Load up the controllers so our server actually uses them!
    app.register_blueprint(db_commands)
    app.register_blueprint(user_bp)

    return app

