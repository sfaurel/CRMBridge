from flask_restx import Namespace, fields


class StatusModel:
    api = Namespace('status', description='Service status operations')
    status_model = api.model('Status', {
        'status': fields.String(description='service status'),
        'message': fields.String(description='status description'),
    })
