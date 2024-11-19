from flask_restx import Namespace, fields


class StatusDto:
    api = Namespace('status', description='Service status operations')
    status = api.model('status', {
        'status': fields.String(description='service status'),
        'message': fields.String(description='status description'),
    })
