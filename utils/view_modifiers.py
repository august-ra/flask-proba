from functools import wraps

import flask
import werkzeug
import werkzeug.wrappers


def use_template(*, mimetype: str = None, filename: str = None):
    def use_template_inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            if isinstance(response, flask.Response | werkzeug.wrappers.Response):
                return response

            is_dict = isinstance(response, dict)

            if is_dict:
                model = response
            else:
                model = dict()

            if filename:
                if not is_dict:
                    raise Exception("Invalid return type {}, we expected a dict as return value.".format(type(response)))

                response = flask.render_template(filename, **response)

            response = flask.make_response(response)
            response.model = model

            if mimetype:
                response.mimetype = mimetype

            return response

        return wrapper

    return use_template_inner
