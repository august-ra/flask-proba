from flask import Flask
from flask_restful import Api

from src.routes import films, smoke

app = Flask(__name__)

api = Api(app)
smoke.add_routes(api)
films.add_routes(api)
