from ..models.users_models import User
from ..services.blacklist_service import blacklist_token


class Auth:

    @staticmethod
    def login_user(data):
        """
        Login user
        Args:
            data (dict): dictionary with username
        Returns:
            On Success:
                A dictionary with auth token.
            On Error
                A dictionary with the error.
        """
        try:
            # fetch the user data
            user = User.query.filter_by(username=data.get('username')).first()
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    response = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token
                    }
                    return response, 200
            else:
                response = {
                    'status': 'fail',
                    'message': 'username or password does not match.'
                }
                return response, 401

        except Exception:
            response = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response, 500

    @staticmethod
    def logout_user(data):
        """
        Logout user
        Args:
            data (str): auth token
        Returns:
            On Success:
                A dictionary with success message.
            On Error
                A dictionary with the error.
        """
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return blacklist_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response, 403

    @staticmethod
    def get_logged_in_user(new_request):
        """TODO"""
        # get the auth token
        data = new_request.headers.get('Authorization')
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)

            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response = {
                    'status': 'success',
                    'data': {
                        'username': user.username,
                    }
                }
                return response, 200
            response = {
                'status': 'fail',
                'message': resp
            }
            return response, 401
        else:
            response = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response, 401

    @staticmethod
    def save_new_user(data):
        """TODO"""
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
