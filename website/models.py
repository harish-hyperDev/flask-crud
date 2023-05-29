from .app import db

class UserAccount(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    full_name=db.Column(db.String(255), nullable=False)
    username=db.Column(db.String(255), unique=True, nullable=False)
    email=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'User("{self.id}","{self.full_name}","{self.username}","{self.email}")'
    
# create admin Class
class AdminAccount(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'Admin("{self.id}","{self.username}","{self.email}")'
