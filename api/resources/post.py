from flask import Blueprint
from marshmallow import pprint

from api.utils import catch_exception
from api.resources import LIMIT_ROWS
from api.database import get_session
from api.models.user import ViewUserContact, UserInfoAll

post_bp = Blueprint('post', __name__, url_prefix='/post')
