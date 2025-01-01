from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<string:name>")
def index(name: str = None):
    if name is None:
        name = "World"

    return f"Hello, {name.capitalize()}!"


if __name__ == "__main__":
    app.run()
