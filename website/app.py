from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

from .config import Config
from .users.main import users


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(users, url_prefix='/home')

# localhost:5000/home

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import UserAccount, AdminAccount

@login_manager.user_loader
def load_user(user_id):
    print("\n LOADING USER \n")
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return UserAccount.query.get(int(user_id))


app.app_context().push()
db.create_all()

admin = Admin(app, name='CRUD APP', template_mode='bootstrap4')


# from .views import views
# from .auth import auth

# admin.add_view(ModelView(views, db.session, endpoint='/'))
# admin.add_view(ModelView(auth, db.session))

# app.register_blueprint(views, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/')