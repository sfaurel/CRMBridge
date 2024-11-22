from flask import Blueprint, render_template
from flask_restx import Api

from app.controllers.status_controller import status_ns
from app.controllers.leads_controller import leads_ns
from app.controllers.users_controller import users_ns
from app.controllers.auth_controller import auth_ns
from app import create_app, db


blueprint = Blueprint("CRM api", __name__, url_prefix="/api/")

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api = Api(
    blueprint,
    version="1.0",
    title="CRM Bridge Api",
    description="API to integrate with a CRM",
    authorizations=authorizations,
    security='apikey'
)


api.add_namespace(status_ns, path='/status')
api.add_namespace(leads_ns, path='/leads')
api.add_namespace(users_ns, path='/users')
api.add_namespace(auth_ns)

app = create_app()
app.register_blueprint(blueprint)


@app.route("/")
def landing_page():
    """
    Renders the landing page to guide users to the API documentation and endpoints.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
