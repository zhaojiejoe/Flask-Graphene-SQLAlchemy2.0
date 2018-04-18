from flask import Flask, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.wrappers import Response
from werkzeug.routing import BaseConverter
from app import settings

db = SQLAlchemy()


class JSONResponse(Response):
    """
    reset the default response type for dict
    """
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
            cls.default_mimetype = 'application/json'
        return super(JSONResponse, cls).force_type(response, environ)


class ListConverter(BaseConverter):
    """
    define a custom spliting style for list
    """

    def __init__(self, url_map, separator=','):
        super(ListConverter, self).__init__(url_map)
        self.separator = separator

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(BaseConverter.to_url(self, value) for value in self.to_python(values))


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.response_class = JSONResponse
    app.url_map.converters['list'] = ListConverter
    db.init_app(app)
    return app
