from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .users.main import users


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(users, url_prefix='/home')

# localhost:5000/home

db = SQLAlchemy(app)

from .models import User

app.app_context().push()
db.create_all()
