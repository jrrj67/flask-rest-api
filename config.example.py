class Config(object):
    ENV = 'development'
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'random_secret_key'


class ProductionConfig(Config):
    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
