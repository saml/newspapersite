from flask import Flask

from . import settings
from . import authors

def create_app(config=None, blueprints=None):
    app = Flask(__name__)
    configure_app(app, config)
    configure_blueprints(app)
    return app

def configure_app(app, config=None):
    app.config.from_object(settings.Default)
    app.config.from_pyfile('settings_local.cfg', silent=True)
    if config:
        app.config.from_object(config)

def configure_blueprints(app):
    app.register_blueprint(authors.bp, url_prefix='/authors')
