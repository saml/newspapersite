import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class Default(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'data.db')
