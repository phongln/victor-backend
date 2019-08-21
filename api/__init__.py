import os
from flask import Flask
from dotenv import load_dotenv

from api.config import get_config
from api.resources import api
from api.database import db


APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


def create_app():
    app = Flask(__name__)
    config = get_config('development')
    app.config.from_object(config())

    db.init_app(app)

    api.init_app(app)
    from api.resources.user import user_bp

    app.register_blueprint(user_bp, url_prefix='/user')

    return app
