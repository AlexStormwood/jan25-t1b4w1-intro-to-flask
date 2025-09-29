# jan25-t1b4w1-intro-to-flask
Intro to Flask and API basics

# Setup Steps

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

