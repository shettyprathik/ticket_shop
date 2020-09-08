from flask import request, jsonify
from pydantic import ValidationError
from src import app
from src.validators.user_request_validator import UsrReqValid
from src.models.user import User
from src.errors.request_validation_error import RequestValidationError
from src.errors.bad_request_error import BadRequestError


@app.route('/api/users/signup', methods=['POST'])
def signup():
    try:
        req = request.get_json() or {}
        usr = UsrReqValid(**req)

        existing_usr = User.objects(email=usr.email)
        if existing_usr:
            raise BadRequestError('Existing User')

        new_usr = User(**usr.dict())
        new_usr.hash_password()
        new_usr.save()

        return new_usr.response()

    except ValidationError as e:
        raise RequestValidationError(e.errors())
