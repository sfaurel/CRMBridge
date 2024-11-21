from .. import db
from ..models.users_models import User


def save_new_user(data):
    """create new user"""
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        new_user = User(
            username=data['username'],
            password=data['password'],
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    """get all users"""
    return User.query.all()


def get_a_user(username):
    """get user by username"""
    return User.query.filter_by(username=username).first()


def generate_token(user):
    """generate new token for username"""
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token
        }
        return response_object, 201
    except Exception:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    """apply changes to bd"""
    db.session.add(data)
    db.session.commit()
