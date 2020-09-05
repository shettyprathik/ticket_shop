from flask import request, jsonify
from pydantic import ValidationError
from bson.json_util import dumps
from src import app, mongo
from src.models.user import UserModel
from src.errors.request_validation_error import RequestValidationError


@app.route('/api/users/signup', methods=['POST'])
def signup():

    try:
        req = request.get_json()
        usr = UserModel(**req)
        usr = usr.dict()

        existing_usr = mongo.db.user.find_one(usr)
        if existing_usr:
            print(existing_usr, flush=True)
            return dumps(existing_usr)

        mongo.db.user.insert_one(usr)
        return dumps(usr)

    except ValidationError as e:
        raise RequestValidationError(e.errors())
