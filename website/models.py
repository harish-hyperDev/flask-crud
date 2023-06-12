from .app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id=db.Column(db.String(500), primary_key=True)
    full_name=db.Column(db.String(255), nullable=False)
    username=db.Column(db.String(255), unique=True, nullable=False)
    email=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'User("{self.id}","{self.full_name}","{self.username}","{self.email}","{self.password}")'
    
