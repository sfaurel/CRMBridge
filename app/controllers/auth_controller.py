from flask import request
from flask_restx import Resource

from ..services.auth_service import Auth
from ..models.auth_models import AuthModel

auth_ns = AuthModel.api
auth_model = AuthModel.auth_model
login_response_model = AuthModel.login_response_model
logout_response_model = AuthModel.logout_response_model


@auth_ns.route('/login')
class UserLogin(Resource):
    """
    User Login Resource
    """
    @auth_ns.doc('user login')
    @auth_ns.expect(auth_model, validate=True)
    @auth_ns.response(code=200, description='Success', model=login_response_model)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@auth_ns.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @auth_ns.doc('logout a user', security='apikey')
    @auth_ns.response(code=200, description='Success', model=logout_response_model)
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
