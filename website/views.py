from flask import render_template
from flask_login import login_required, current_user

from .app import app
# from flask import Blueprint

# views = Blueprint('views', __name__)

@app.route('/')
def index():
    return  render_template('base.html')

@app.route('/home')
def home():
    return render_template('user/welcome.html')

