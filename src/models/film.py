import uuid

from src import db


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False, index=True)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f"Film({self.id}, {self.title}, {self.year})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "uuid": self.uuid,
        }
