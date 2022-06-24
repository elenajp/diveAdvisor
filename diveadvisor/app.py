from flask import Flask
import resources

app = Flask(__name__)

app.add_url_rule("/", view_func=resources.home)
app.add_url_rule("/login", view_func=resources.login)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
