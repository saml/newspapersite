"""
Creates shell using IPython
"""
import sys

from werkzeug import script

from newspapersite import create_app
from newspapersite.extensions import db

def make_shell():
    return dict(app=create_app(), db=db)

if __name__ == "__main__":
    script.make_shell(make_shell, use_ipython=True)()
