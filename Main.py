from flask import Flask
from markupsafe import escape

app=Flask(__name__)
@app.route("/")
def index():
    return "Index Page"
@app.route("/hello")
def hello_world():
    return "<p>Hello world</p>"
@app.route("/hello/<name>")
def name(name):
    return f"Please Enter name:{escape(name)}"
@app.route("/User/<username>")
def user_profile(username):
    return f"User {escape(username)}"

if __name__ == "__main__":
    app.run(debug=True)