from .. import db

from app.models.blacklist_models import BlacklistToken


def blacklist_token(token):
    """
    Store token avoiding authenticate whit this token
    Args:
        token (str): the blacklisted token
    """
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 200
