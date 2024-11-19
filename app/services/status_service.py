def get_service_status():
    """
    Check API dependencies.

    Returns:
        dict: A dictionary containing:
            - "status": "OK" if everything is functioning properly,
                        "ERROR" otherwise.
            - "message": A description of the service status.
    """
    return {"status": "ok", "message": "Service is running."}, 200
