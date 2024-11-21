
from .. import db, flask_bcrypt
import datetime
import jwt
from flask_restx import Namespace, fields

from ..utils.conf import SECRET_KEY
from ..models.blacklist_models import BlacklistToken


class UserModel:
    api = Namespace('user', description='User operations')
    user_model = api.model('User', {
        'username': fields.String(required=True, description='user username'),
    })
    login_user_model = api.model('LoginUser', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })
    user_registered_model = api.model('UserRegistered', {
        'status': fields.String(description='Status of the response', example='success'),
        'message': fields.String(description='Message of the response', example='Successfully registered.'),
        'Authorization': fields.String(description='JWT Token for Authorization', example='your_jwt_token_here')
    })


class User(db.Model):
    """ User database Model"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        """store hashed password"""
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check if inserted password is correct"""
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token

        Returns:
            string: user auth token
        """
        try:
            payload = {
                'exp': datetime.datetime.now() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.now(),
                'sub': str(user_id)
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        Args:
            auth_token (str): user auth token
        Returns:
            integer|string
        """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return int(payload['sub'])
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
