from src import app
from flask import jsonify
from pydantic import BaseModel
from typing import List, Optional

class ErrorSingle(BaseModel):
    message: str
    field: Optional[str]

class ErrorList(BaseModel):
    errors: List[ErrorSingle]

@app.errorhandler(Exception)
def handle_error(err):
    serialize_errors = err.serialize_errors()
    ErrorList(errors=serialize_errors)
    return jsonify(serialize_errors)