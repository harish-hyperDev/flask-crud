from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from website.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from .models import User

app.app_context().push()
db.create_all()
