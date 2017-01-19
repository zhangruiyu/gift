from flask import Flask

from app.extensions.database import db
from app.models import (Family, Comments)
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 初始化数据库
    initDatabse(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


def initDatabse(app):
    from app.extensions.database import db
    db.init_app(app)
    db.create_all()
