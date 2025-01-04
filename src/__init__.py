from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from config import Config


SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.yaml"
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Flask Proba",
    }
)

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

from src import models, routes
