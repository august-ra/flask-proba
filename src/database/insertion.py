from src import db
from src.models.film import Film


def insert_film():
    film = Film("test", 2025)
    db.session.add(film)
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    insert_film()
