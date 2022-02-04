from flask import Flask
from flask_restx import Api
from flask import Blueprint
from .controller import ns

def create_api():
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(
        blueprint,
        title='Book service',
        version='1.0',
        description='Service for my library management.',
    )

    # TODO
    api.add_namespace(ns, path="")

    return blueprint


def create_app():
    app = Flask(__name__)
    api = create_api()

    app.register_blueprint(api)

    return app
