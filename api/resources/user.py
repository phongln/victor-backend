from flask import Blueprint, jsonify
from flask_restful import Resource

from api.database import load_session


user_bp = Blueprint('user', __name__, url_prefix='/user')


class UserResource(Resource):
    def get(self, user_id):
        return get_user(user_id)


# @user_bp.route('/<int:user_id>')
def get_user(user_id):
    from api.models.user import UserProfile
    session = load_session()
    respone = session.query(UserProfile).all()

    return UserProfile.jsonify(respone)
