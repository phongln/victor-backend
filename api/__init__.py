from flask import Flask, g
from flask_cors import CORS

from api.config import config
from api.celery import make_celery


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    celery = make_celery(app)

    with app.app_context():

        CORS(app)

        from api.database import init_datatabase
        init_datatabase(app)

        from api.resources import init_resources
        init_resources(app)

    return app


app = create_app()
