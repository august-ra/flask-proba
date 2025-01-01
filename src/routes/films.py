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


class Films(Resource):
    def get(self, uuid: int = None):
        films = get_matrix_films()

        if uuid is None:
            return {"films": films}, 200
        elif not isinstance(uuid, int) or uuid <= 0 or uuid > len(films):
            return {"message": "Film not found"}, 404
        else:
            return films[uuid + 1], 200


def add_routes(api):
    api.add_resource(Films, "/api/films", "/api/films/<int:uuid>", "/api/films/<uuid>", strict_slashes=False)
