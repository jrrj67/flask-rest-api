class Config(object):
    ENV = 'production'
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'random_secret_key'

    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
