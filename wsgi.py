from flask import Flask

from utils.view_modifiers import use_template

app = Flask(__name__)


@app.route("/")
@app.route("/<string:name>")
def index(name: str = None):
    if name is None:
        name = "World"

    return f"Hello, {name.capitalize()}!"


@app.route("/matrix")
@use_template(filename="films.html")
def matrix():
    return {
        "films": get_matrix_films(),
    }


def get_matrix_films():
    return [
        {
            "title": "The Matrix",
            "year": 1999,
        },
        {
            "title": "The Matrix Reloaded",
            "year": 2003,
        },
        {
            "title": "The Matrix Revolutions",
            "year": 2003,
        },
        {
            "title": "The Animatrix",
            "year": 2003,
        },
    ]


if __name__ == "__main__":
    app.run()
