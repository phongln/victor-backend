from functools import wraps, partial
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from api.config import POSTGRES_DATABASE_URI

db = SQLAlchemy()
ma = Marshmallow()


def get_session(func=None, *deco_args, **deco_kwargs):
    if func is None:
        return partial(get_session, *deco_args, **deco_kwargs)

    @wraps(func)
    def wrapper(*args, **kwargs):
        session = db.Session()
        return func(session, *args, **kwargs)

    return wrapper


def init_datatabase(app):
    db.init_app(app)
    db.Session = scoped_session(sessionmaker(bind=db.engine))
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.Session.remove()

    ma.init_app(app)
