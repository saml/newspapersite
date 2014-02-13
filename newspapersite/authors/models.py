from ..extensions import db

class Author(db.Model):
    __tablename__ = 'authors_author'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(32), unique=True)
    twitter = db.Column(db.String(50))
    gplus = db.Column(db.String(120))

