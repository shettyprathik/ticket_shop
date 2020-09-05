from src import app
from flask import jsonify
from pydantic import BaseModel
from typing import List, Optional


class ErrorSingleSchema(BaseModel):
    message: str
    field: Optional[str]


class ErrorListSchema(BaseModel):
    errors: List[ErrorSingleSchema]


@app.errorhandler(Exception)
def handle_error(err):
    serialize_errors = err.serialize_errors()
    error_out = ErrorListSchema(errors=serialize_errors).dict()['errors']
    return jsonify(error_out)
