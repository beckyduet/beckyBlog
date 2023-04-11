import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  #最好写在环境变量中
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '25'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'biqinliu@163.com'  #最好写在环境变量中
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'NXPPEQXZUYECYVQB'  #最好写在环境变量中
    FLASKY_MAIL_SUBJECT_PREFIX = '[Becky]'
    FLASKY_MAIL_SENDER = 'Becky Admin <biqinliu@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'biqinliu@163.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #在不需要跟踪对象变化时降低内存消耗
    FLASKY_POSTS_PER_PAGE = 4
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    BOOTSTRAP_BOOTSWATCH_THEME = 'morph'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
