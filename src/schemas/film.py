from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema

from src.models.film import Film


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        load_instance = True
