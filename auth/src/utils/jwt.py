import functools
from src import verify_jwt_in_request
from src.errors.token_error import TokenError


def verify_jwt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return func(*args, **kwargs)
        except:
            raise TokenError("Token Error")

    return wrapper
