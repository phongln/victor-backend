from flask import Blueprint

from api.utils import catch_exception
from api.resources import LIMIT_ROWS
from api.database import get_session
from api.models import jsonify_respone
from api.models.meta import ViewAllRefTable


meta_bp = Blueprint('meta', __name__, url_prefix='/meta')


@meta_bp.route('/', strict_slashes=False)
@catch_exception
@get_session
def get_all_ref_table(session):
    respone = session.query(ViewAllRefTable).all()

    return jsonify_respone(respone, many=True)
