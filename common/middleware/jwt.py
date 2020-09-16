import functools
from flask_jwt_extended import verify_jwt_in_request
from common.errors.token_error import TokenError


def verify_jwt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except:
            raise TokenError("Token Error")
        return func(*args, **kwargs)
    return wrapper
