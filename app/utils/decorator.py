import requests
from functools import wraps


def handle_request_errors(func):
    """Decorator to handle errors during an outgoing HTTP request."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            # Handle request-related errors
            print(f"Request failed: {e}")
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
            print(f"Unexpected error: {e}")
            return {"status": "error", "message": "Unexpected error"}
    return wrapper
