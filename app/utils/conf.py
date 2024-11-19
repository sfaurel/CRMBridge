from dotenv import load_dotenv
import os


def load_config(app):
    """Load flask conf from .env."""
    load_dotenv()
    app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
