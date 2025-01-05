from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.models.film import Film
from src.schemas.film import FilmSchema


class Films(Resource):
    schema = FilmSchema()

    def response_with_all_films(self):
        films = db.session.query(Film).all()
        films = self.schema.dump(films, many=True)
        return {"films": films}, 200

    def response_with_film(self, film: Film = None):
        if film is None:
            return self.response_cannot_find()
        else:
            return self.schema.dump(film), 200

    @staticmethod
    def response_cannot_find():
        return {"message": "Film not found"}, 404

    @staticmethod
    def response_cannot_create():
        return {"message": "Wrong data to add film"}, 400

    def get(self, text: int | str = None):
        if text is None:
            return self.response_with_all_films()
        elif isinstance(text, str):
            film = db.session.query(Film).filter_by(uuid=text).first()

            if film:
                return film.to_dict(), 200

            film = db.session.query(Film).filter(Film.title.contains(text)).first()
            return self.response_with_film(film)
        elif isinstance(text, int):
            film = db.session.query(Film).filter_by(id=text).first()
            return self.response_with_film(film)
        else:
            return self.response_with_film()

    def post(self):
        data = request.json

        try:
            film = self.schema.load(data, session=db.session)
        except ValidationError as error:
            return {"message": str(error)}, 400

        db.session.add(film)
        db.session.commit()

        return self.response_with_all_films()

    def delete(self, text: str = None):
        if text is None:
            return self.response_cannot_find()

        film = db.session.query(Film).filter_by(uuid=text).first()

        if film is None:
            return self.response_cannot_find()

        db.session.delete(film)
        db.session.commit()

        return self.response_with_all_films()
