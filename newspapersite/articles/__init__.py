from flask import Blueprint

bp = Blueprint('articles', __name__)

@bp.route('/')
def index():
    return 'list of articles'
