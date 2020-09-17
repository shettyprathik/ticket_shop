import functools
from flask_jwt_extended import get_jwt_identity
from flask import request


def get_current_user(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            request.current_user = get_jwt_identity()
        except:
            request.current_user = "null"
        return func(*args, **kwargs)
    return wrapper
