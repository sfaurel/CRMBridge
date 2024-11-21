import requests
from flask import request
from functools import wraps

from ..services.auth_service import Auth


def handle_request_errors(func):
    """Decorator to handle errors during an outgoing HTTP request."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            # Handle request-related errors
            error_response = {
                "status": "error",
                "message": "Unknown error"
            }
            if hasattr(e, "response") and e.response is not None:
                try:
                    error_data = e.response.json()
                    error_response["message"] = error_data.get("error", "Unknown error")
                    error_response["details"] = error_data.get("details", "No additional details available")
                except ValueError:  # Response is not a valid JSON
                    error_response["message"] = "Failed to parse error details from response"
            return error_response

        except Exception as e:
            # Handle any other unexpected errors
            return {"status": "error", "message": "Unexpected error"}
    return wrapper


def token_required(func):
    """Decorator to check if the user is logged in. Apply to endpoints where required."""

    @wraps(func)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return func(*args, **kwargs)

    return decorated
