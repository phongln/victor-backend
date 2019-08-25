from flask import Flask

from api.config import get_config


def create_app():
    app = Flask(__name__)
    config = get_config()
    app.config.from_object(config)

    with app.app_context():
        from api.database import db, ma
        db.init_app(app)
        ma.init_app(app)

        from api.resources import api, init_blueprint
        api.init_app(app)
        init_blueprint(app)

    return app


app = create_app()
