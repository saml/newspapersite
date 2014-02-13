from flask import Blueprint

from .models import Author

bp = Blueprint('users', __name__)

@bp.route('/')
def index():
    return 'list of authors'
