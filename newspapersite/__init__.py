from flask import Flask

from . import users, tags, articles, images

def create_app(config=None, blueprints=None):
    app = Flask(__name__)
    configure_app(app, config)
    configure_blueprints(app)
    return app

def configure_app(app, config=None):
    app.config.from_object('newspapersite.settings')
    app.config.from_pyfile('settings_local.cfg', silent=True)
    app.config.from_envvar('NEWSPAPERSITE_SETTINGS', silent=True)
    if config:
        app.config.from_object(config)

def configure_blueprints(app):
    app.register_blueprint(users.bp,        url_prefix='/users')
    app.register_blueprint(tags.bp,         url_prefix='/tags')
    app.register_blueprint(articles.bp,     url_prefix='/articles')
    app.register_blueprint(images.bp,       url_prefix='/images')
