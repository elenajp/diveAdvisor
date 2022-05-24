from __init__ import app


@app.route("/hello")
def hello():
    return "Hello, World!"


@app.route("/")
def home():
    return ""


@app.route("/login")
def login():
    return ""


@app.route("/logout")
def logout():
    return ""


@app.route("/profile")
def profile():
    return ""
