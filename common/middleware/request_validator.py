import functools
from flask import request
from common.errors.request_validation_error import RequestValidationError
from pydantic import ValidationError


def request_validator(ValidatorSchema):

    def wrapper(func):

        @functools.wraps(func)
        def validate(*args, **kwargs):
            try:
                req = request.get_json() or {}
                request.valid_body = ValidatorSchema(**req)

            except ValidationError as e:
                raise RequestValidationError(e.errors())

            return func(*args, **kwargs)
        return validate

    return wrapper
