from flask import Flask, jsonify

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, pizza!</p>"


# http://localhost:5000/articles/
@app.route("/articles")
def article_demo_function():
    # 1. Query the database for articles
    # 2. Process the result to make sure it's a list of data 
    # 3. Return the list 

    return jsonify([
        {
            "title":"Example Article 1",
            "content":"Blah blah blah",
            "author":"130489u23topi2"
        },
        {
            "title":"Example Article 2",
            "content":"Blah 2 blah blah 2",
            "author":"3405398urfgop"
        }
    ])


@app.route("/bananas", methods=["POST"])
def post_bananas():
    return jsonify({
        "message":"Post bananas!"
    })