from flask_restx import Namespace, fields


class AuthModel:
    api = Namespace('auth', description='Authentication operations')
    auth_model = api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password'),
    })

    login_response_model = api.model('LoginResponse', {
        'status': fields.String(description='Status of the response', example='success'),
        'message': fields.String(description='Message of the response', example='Successfully logged in.'),
        'Authorization': fields.String(description='JWT Token for Authorization', example='your_jwt_token_here')
    })

    logout_response_model = api.model('LogoutResponse', {
        'status': fields.String(description='Status of the response', example='success'),
        'message': fields.String(description='Message of the response', example='Successfully logged out.'),
    })
