from src import api
from src.resources.films import Films
from src.resources.smoke import Smoke

api.add_resource(Smoke, "/api/smoke", strict_slashes=False)
api.add_resource(Films, "/api/films", "/api/films/<int:text>", "/api/films/<text>", strict_slashes=False)
