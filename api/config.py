import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
DOTENV_PATH = os.path.join(APP_ROOT, '.env')
load_dotenv(DOTENV_PATH)

FLASK_ENV = os.getenv('FLASK_ENV')

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

POSTGRES_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = POSTGRES_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'prodction': ProductionConfig,
    'testing': TestingConfig
}


def get_config():
    return config[FLASK_ENV]
