from flask import request
from flask_restful import Resource

from src import api, db
from src.models.film import Film


def find_by_title(films, title):
    films = filter(lambda f: title.lower() in f["title"].lower(), films)

    try:
        film = next(films)
        return film, 200
    except StopIteration:
        return {"message": "Film not found"}, 404


class Films(Resource):
    @staticmethod
    def response_with_all_films():
        films = db.session.query(Film).all()
        films = [f.to_dict() for f in films]
        return {"films": films}, 200

    @staticmethod
    def response_with_film(film: Film = None):
        if film is None:
            return {"message": "Film not found"}, 404
        else:
            return film.to_dict(), 200

    @staticmethod
    def response_cannot_create():
        return {"message": "Wrong data to add film"}, 400

    def get(self, text: int | str = None):
        if text is None:
            return self.response_with_all_films()
        elif isinstance(text, str):
            film = db.session.query(Film).filter(Film.title.contains(text)).first()
            return self.response_with_film(film)
        elif isinstance(text, int):
            film = db.session.query(Film).filter_by(id=text).first()
            return self.response_with_film(film)
        else:
            return self.response_with_film()

    def post(self):
        data = request.json

        if not data:
            return self.response_cannot_create()

        try:
            film = Film(**data)

            db.session.add(film)
            db.session.commit()
        except (ValueError, KeyError):
            return self.response_cannot_create()

        return self.response_with_all_films()


api.add_resource(Films, "/api/films", "/api/films/<int:text>", "/api/films/<text>", strict_slashes=False)
