from flask import Blueprint, g
from api import tasks

test_bp = Blueprint('test', __name__, url_prefix='/test')


@test_bp.route('/', strict_slashes=False)
def index():
    if 'celery' in g:
        print(dir(g.celery))
    else:
        print('Not exist celery')
    result = tasks.very_long_task.delay(10)

    return {'200': 'ok'}
