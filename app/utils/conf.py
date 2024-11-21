from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))


def load_config(app):
    """Load flask conf from .env."""
    load_dotenv()
    app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'CRMBridge.db')


SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
