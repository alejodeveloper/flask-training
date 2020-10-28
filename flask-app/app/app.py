from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .models import UserModel


def load_user(username):
    return UserModel.query(username)


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)

    return app
