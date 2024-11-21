from flask import Flask
from app.utils.conf import load_config


def create_app():
    app = Flask(__name__)

    load_config(app)

    return app
