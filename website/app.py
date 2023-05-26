from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

from .config import Config
from .users.main import users


app = Flask(__name__)
app.config.from_object(Config)

# localhost:5000/home
app.register_blueprint(users, url_prefix='/home')

db = SQLAlchemy(app)
from .models import UserAccount, AdminAccount

app.app_context().push()
db.create_all()

admin = Admin(app, name='CRUD APP', template_mode='bootstrap4')


# from .views import views
# from .auth import auth

# admin.add_view(ModelView(views, db.session, endpoint='/'))
# admin.add_view(ModelView(auth, db.session))

# app.register_blueprint(views, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/')