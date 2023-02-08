"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.model):

    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    
    first_name = db.Column(db.String(40), nullable=False)
    
    last_name = db.Column(db.String(40), nullable=False)

    image_url = db.Column(db.Text)

