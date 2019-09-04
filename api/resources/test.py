from flask import Blueprint, jsonify
from api import tasks

test_bp = Blueprint('test', __name__, url_prefix='/test')


@test_bp.route('/', strict_slashes=False)
def index():
    result = tasks.very_long_task.delay(10)
    respone = jsonify({
        'message': 'first end point "test" is called',
        'status_code': 200
    })

    return respone
