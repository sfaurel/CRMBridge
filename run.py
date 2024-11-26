from flask import Blueprint, redirect
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
    description=(
        "This API is a integration with a CRM system for lead management.\n\n"
        "Use /users to create a new user\n"
        "/leads and GET /users are protected endpoints \n\n"
        "**Authentication:**\n"
        "Protected endpoints require a JWT token for access. To obtain the token:\n"
        "1. Use the endpoint **`POST /auth/login`** with user credentials.\n"
        "2. Copy the token provided in the response.\n"
        "3. Use the token in the **'Authorize'** button of this documentation, with the format: `Bearer <token>`."
    ),
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
    Redirects to the API documentation.
    """
    return redirect("/api")


if __name__ == "__main__":
    app.run()
