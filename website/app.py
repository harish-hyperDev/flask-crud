from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# session['API_KEY'] = "flask-insecure?da471aa9-ac0b-4cee-a572-33cbae58043a"

db = SQLAlchemy(app)

from .models import User

app.app_context().push()
db.create_all()
