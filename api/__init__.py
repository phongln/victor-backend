from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    INTEGER = db.Integer
    STRING = db.String
    print(dir(INTEGER))

    @app.route("/")
    def index():
        return "hello victor"

    return app
