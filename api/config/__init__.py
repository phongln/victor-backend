import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
DOTENV_PATH = os.path.join(APP_ROOT, '.flaskenv')
load_dotenv(DOTENV_PATH)


FLASK_ENV = os.getenv('FLASK_ENV')

API_HOST = os.getenv('API_HOST')
API_PORT = os.getenv('API_PORT')

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

POSTGRES_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'



def get_gunicornconfig():
    from . import gunicornconfig

    return gunicornconfig


def get_config():
    from .development import DevelopmentConfig
    from .production import ProductionConfig
    from .testing import TestingConfig

    _config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    return _config[FLASK_ENV]


config = get_config()
gunicornconfig = get_gunicornconfig()