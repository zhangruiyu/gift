import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # （ 用来在每次请求结束时候提交数据库改动，通常设置为True）
    # DBA_URL = 'redis://localhost:6379/1'
    REDIS_URL = "redis://localhost:6379/0"

    QINIU_ACCESS_KEY = 'FYM-dD4iIjaRPikS0oxsfBSZYj6Xh3I1tABFZ_Fh'
    QINIU_SECRET_KEY = 'cdGmr97dMP_04G38MCeQmD5RCWnUHvy2OC4urhN4'
    QINIU_BUCKET_NAME = 'kindergartenavatar'
    QINIU_BUCKET_DOMAIN = 'of6a384fd.bkt.clouddn.com'

    # 在调试模式下，Flask-SQLAlchemy将会记录所有的SQL查询。当请求出错或进行单元测试时，这些信息非常有用。将SQLALCHEMY_RECORD_QUERIES设置为True时，将关闭数据库的调试模式。
    # SQLALCHEMY_RECORD_QUERIES = True

    # FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://zryzs:woaiwojia520@localhost/gift'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://zryzs:woaiwojia520@localhost/gift'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woaiwojia520@localhost/gift'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
