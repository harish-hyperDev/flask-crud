from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # admin = Admin(app)
    db = SQLAlchemy(app)
    admin = Admin(app, name='CRUD APP', template_mode='bootstrap4')

    from .views import views
    from .auth import auth
    
    admin.add_view(ModelView(views, db.session))
    admin.add_view(ModelView(auth, db.session))
    
    # app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')
    return app