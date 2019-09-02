from flask import Blueprint
from marshmallow import pprint

from api.utils import catch_exception
from api.resources import LIMIT_ROWS
from api.database import get_session
from api.models import jsonify_respone
from api.models.user import JsonUserContact, UserInfoAll


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', strict_slashes=False)
@catch_exception
@get_session
def get_user_all(session):
    respone = session.query(UserInfoAll).limit(LIMIT_ROWS).all()

    return jsonify_respone(respone, many=True)


@user_bp.route('/<int:user_id>', strict_slashes=False)
@catch_exception
@get_session
def get_user(session, user_id):
    respone = session.query(UserInfoAll).filter_by(user_id=user_id).one()

    return jsonify_respone(respone)


@user_bp.route('/<int:user_id>/contact', strict_slashes=False)
@catch_exception
@get_session
def get_user_contact(session, user_id):
    respone = session.query(JsonUserContact).filter_by(user_id=user_id).all()

    return jsonify_respone(respone, many=True)
