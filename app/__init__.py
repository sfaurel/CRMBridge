from flask import Blueprint
from flask_restx import Api

from .controllers.status_controller import status_ns
from .controllers.leads_controller import leads_ns

blueprint = Blueprint("CRM api", __name__, url_prefix="/api/")

api = Api(
    blueprint,
    version="1.0",
    title="CRM Api",
    description="API to integrate with a CRM",
)

api.add_namespace(status_ns, path='/status')
api.add_namespace(leads_ns, path='/leads')
