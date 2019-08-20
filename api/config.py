

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blog_api:Aa123456@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blog_api:Aa123456@localhost/blog'


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'prodction': ProductionConfig,
    'testing': TestingConfig
}


def get_config(flask_env='development'):
    return config[flask_env]
