from sqlalchemy.orm import exc as orm_exc
from flask import abort
from functools import wraps
import traceback


def catch_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except orm_exc.NoResultFound:
            abort(404)
        except Exception:
            traceback.print_exc()

    return wrapper
