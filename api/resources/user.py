from flask import Blueprint, jsonify
from flask_restful import Resource

from api.database import db
from api.models.user import UserProfile

user_bp = Blueprint('user', __name__, url_prefix='/user')


class UserResource(Resource):
    def get(self):
        return {}


@user_bp.route('/<int:user_id>')
def get_user(user_id):
    return str(dir(UserProfile.query.get(user_id)))
