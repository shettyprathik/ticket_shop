import functools
from flask import request
from src.errors.request_validation_error import RequestValidationError
from pydantic import ValidationError


def request_validator(ValidatorSchema):

    def wrapper(func):

        @functools.wraps(func)
        def validate(*args, **kwargs):
            try:
                req = request.get_json() or {}
                request.valid_body = ValidatorSchema(**req)
                return func(*args, **kwargs)

            except ValidationError as e:
                raise RequestValidationError(e.errors())

        return validate

    return wrapper
