from flask import request
from flask_restful import Resource


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


def find_by_title(films, title):
    films = filter(lambda f: title.lower() in f["title"].lower(), films)

    try:
        film = next(films)
        return film, 200
    except StopIteration:
        return {"message": "Film not found"}, 404


class Films(Resource):
    def get(self, text: int | str = None):
        films = get_matrix_films()

        if text is None:
            return {"films": films}, 200
        elif isinstance(text, str):
            return find_by_title(films, text)
        elif not isinstance(text, int) or text <= 0 or text > len(films):
            return {"message": "Film not found"}, 404
        else:
            return films[text + 1], 200

    def post(self):
        data = request.json
        films = get_matrix_films()
        films.append(data)
        return {"films": films}, 200


def add_routes(api):
    api.add_resource(Films, "/api/films", "/api/films/<int:text>", "/api/films/<text>", strict_slashes=False)
