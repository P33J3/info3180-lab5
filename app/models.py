# Add any model classes for Flask-SQLAlchemy here
from . import db


class Movie(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(256))
    poster = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
