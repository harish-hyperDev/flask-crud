from .app import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(255), nullable=False)
    last_name=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    username=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    confirm_password=db.Column(db.String(255), nullable=False)
    

    def __repr__(self):
        return f'User("{self.id}","{self.first_name}","{self.last_name}","{self.email}","{self.username}")'
    
# create admin Class
class Admin(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    confirm_password=db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'Admin("{self.id}","{self.username}","{self.email}")'
