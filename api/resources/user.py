from functools import wraps
from flask import Blueprint, abort
from flask_restful import Resource
from sqlalchemy.orm import exc as orm_exc
import traceback

from api.database import load_session
from api.models.user import UserProfile, ViewUserProfile


user_bp = Blueprint('user', __name__, url_prefix='/user')


class UserResource(Resource):
    def get(self, user_id):
        return get_user(user_id)


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


@user_bp.route('/<int:user_id>', strict_slashes=False)
@catch_exception
def get_user(user_id):
    session = load_session()
    user = session.query(ViewUserProfile).filter_by(user_id=user_id).one()
    return ViewUserProfile.jsonify(user)


@user_bp.route('/', strict_slashes=False)
@catch_exception
def get_users():
    session = load_session()
    users = session.query(ViewUserProfile).all()

    return ViewUserProfile.jsonify(users, many=True)
