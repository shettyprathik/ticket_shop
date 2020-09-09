from flask import request, jsonify, make_response
from pydantic import ValidationError
from src import app, create_access_token, set_access_cookies
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

        resp = make_response(new_usr.response())
        access_token = create_access_token(identity=str(new_usr.id))
        set_access_cookies(resp, access_token)

        return resp, 201

    except ValidationError as e:
        raise RequestValidationError(e.errors())
