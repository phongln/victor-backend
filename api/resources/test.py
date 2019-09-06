from flask import Blueprint, jsonify
from api.tasks import test

test_bp = Blueprint('test', __name__, url_prefix='/test')


@test_bp.route('/', strict_slashes=False)
def index():
    result = test.very_long_task.delay(10)
    respone = jsonify(
        {'message': 'This task only hangs out', 'status_code': '200'})

    return respone


@test_bp.route('/wait', strict_slashes=False)
def wait():
    result = test.very_long_task.delay(10)
    respone = jsonify(
        {'message': 'This task only hangs out', 'status_code': '200'})

    return result.wait()
