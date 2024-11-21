from flask import request
from flask_restx import Resource

from ..utils.decorator import token_required
from ..models.users_models import UserModel
from ..services.users_services import save_new_user, get_all_users

users_ns = UserModel.api
user_model = UserModel.user_model
login_user_model = UserModel.login_user_model
user_registered_model = UserModel.user_registered_model


@users_ns.route('/')
class UserList(Resource):
    @users_ns.doc('list_of_registered_users', security='apikey')
    @token_required
    @users_ns.marshal_list_with(user_model, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @users_ns.expect(login_user_model, validate=True)
    @users_ns.marshal_with(user_registered_model, code=201)
    @users_ns.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)
