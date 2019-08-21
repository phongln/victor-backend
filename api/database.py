from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from api.config import POSTGRES_DATABASE_URI

db = SQLAlchemy()
ma = Marshmallow()


def load_session():
    Session = sessionmaker(bind=db.engine)
    session = Session()

    return session
