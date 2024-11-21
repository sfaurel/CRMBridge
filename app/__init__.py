from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app.utils.conf import load_config


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    load_config(app)
    db.init_app(app)
    flask_bcrypt.init_app(app)
    Migrate(app, db)
    # import models for migration
    from app.models import users_models, blacklist_models

    return app
