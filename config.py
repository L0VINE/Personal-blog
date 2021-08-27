import os

class Config:

    SECRET_KEY='1234'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/blogs'


    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'cynthialovin97@gmail.com'
    MAIL_PASSWORD = 'PAPSI@123'
    SUBJECT_PREFIX = 'Cindy Blog!'
    SENDER_EMAIL = 'cynthialovin97@gmail.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:Access@localhost/blogs'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/blogs'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/blogs'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
