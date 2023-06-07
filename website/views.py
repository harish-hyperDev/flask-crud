from flask import render_template, session
from flask_login import login_required, current_user

from .app import app
# from flask import Blueprint

# views = Blueprint('views', __name__)

@app.route('/')
def index():
    return  render_template('base.html')

@app.route('/home')
def home():
    print("current user : ", current_user.username)
    return render_template('user/home.html')

# route for admin home page
@app.route('/admin/home')
@login_required
def admin_home():
    return render_template('admin/home.html')

