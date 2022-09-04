from flask import Flask
from flask_restful import Api, Resource
from .commands import show_cv
from .routs import Index, Personal, Experience, Education, Languages, Skills


def create_app(config_file = 'settings.py'):
    app = Flask(__name__)

    app.cli.add_command(show_cv)

    api = Api(app)
    api.add_resource(Index, '/')
    api.add_resource(Personal, '/personal')
    api.add_resource(Experience, '/experience')
    api.add_resource(Education, '/education')
    api.add_resource(Languages, '/languages')
    api.add_resource(Skills, '/skills')

    return app
