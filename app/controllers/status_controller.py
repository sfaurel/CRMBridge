from flask_restx import Resource

from ..services.status_service import get_service_status
from ..utils.dto import StatusDto


status_api = StatusDto.api
_status = StatusDto.status


@status_api.route('/')
class Status(Resource):
    @status_api.doc(
        id='server_status',
        description='Endpoint to check service status.'
    )
    @status_api.marshal_with(_status)
    def get(self):
        """Service status check endpoint"""
        return get_service_status()
