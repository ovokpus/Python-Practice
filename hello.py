from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/user/<username>")
def user_page(username):
    return f"Welcome, {username}!"


@app.route("blog/post/<int:post_id>")
def show_post(post_id):
    return f"This is the page for post # {post_id}"
