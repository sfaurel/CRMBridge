from flask import Flask

from app import blueprint
from app.utils.conf import load_config

app = Flask(__name__)
load_config(app)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
