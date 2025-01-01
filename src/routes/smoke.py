from flask_restful import Resource


class Smoke(Resource):
    def get(self):
        return {"message": "OK"}, 200


def add_routes(api):
    api.add_resource(Smoke, "/api/smoke", strict_slashes=False)
