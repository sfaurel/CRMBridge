from flask_restx import Resource

from ..services.status_service import get_service_status
from ..models.status_models import StatusModel


status_ns = StatusModel.api
status_model = StatusModel.status_model


@status_ns.route('/')
class Status(Resource):
    @status_ns.marshal_with(status_model)
    @status_ns.marshal_with(status_model)
    def get(self):
        """
        Service status check endpoint
        TODO add crm health check
        """

        return get_service_status()
