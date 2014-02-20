from flask import Blueprint

bp = Blueprint('tags', __name__)

@bp.route('/')
def index():
    return 'list of tags'
