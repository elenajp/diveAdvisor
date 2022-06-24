from flask import Blueprint

# resources = Blueprint(
#     "resources", __name__, static_folder="static", template_folder="templates"
# )


def home():
    return "This is the home page"


def login():
    return "This is the login page"


# def logout():
#     return ""

# def profile():
#     return ""

# def add_dive_shop():
#     return ""

# def add_dive_shop():
#     return ""
