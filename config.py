import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
  SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASE_DIR / "data" / "flask_proba.sqlite3")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  # SQLALCHEMY_ECHO = True
