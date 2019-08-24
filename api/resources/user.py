from functools import wraps
from flask import Blueprint, abort
from flask_restful import Resource
from sqlalchemy.orm import exc as orm_exc
from marshmallow import pprint
import traceback

from api.database import get_session
from api.models.user import ViewUserProfile, ViewUserContact, UserInfoAll
from api.models.user import UserInfoAllSchema, ViewUserContactSchema

user_bp = Blueprint('user', __name__, url_prefix='/user')


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


@user_bp.route('/', strict_slashes=False)
@catch_exception
@get_session
def get_user_all(session):
    users = session.query(ViewUserProfile).all()
    session.commit()

    return ViewUserProfile.jsonify(users, many=True)


@user_bp.route('/<int:user_id>', strict_slashes=False)
@catch_exception
@get_session
def get_user(session, user_id):
    user_info_all = session.query(UserInfoAll).filter_by(user_id=user_id).one()
    session.commit()

    return user_info_all.json()


@user_bp.route('/<int:user_id>/contact', strict_slashes=False)
@catch_exception
@get_session
def get_user_contact(session, user_id):
    contacts = session.query(ViewUserContact).filter_by(user_id=user_id).all()
    session.commit()

    return ViewUserContact.jsonify(contacts, many=True)
