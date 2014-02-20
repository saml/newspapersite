from flask import Blueprint

bp = Blueprint('images', __name__)

@bp.route('/')
def index():
    return 'list of images'
