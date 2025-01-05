from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models.film import Film


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ["id", "uuid"]
        load_instance = True
