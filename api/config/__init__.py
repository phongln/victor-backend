import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
DOTENV_PATH = os.path.join(APP_ROOT, '.env')
load_dotenv(DOTENV_PATH)


FLASK_ENV = os.getenv('FLASK_ENV')

BLOG_HOST = os.getenv('BLOG_HOST')
BLOG_PORT = os.getenv('BLOG_PORT')

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

POSTGRES_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'



def get_celeryconfig():
    from . import celeryconfig
    
    return celeryconfig

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
celeryconfig = get_celeryconfig()
gunicornconfig = get_gunicornconfig()