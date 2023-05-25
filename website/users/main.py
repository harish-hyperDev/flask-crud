from flask import Blueprint, render_template

users = Blueprint('users', __name__, template_folder='templates')

# localhost:5000/home
@users.route('/')
def welcome():
    return render_template('user/welcome.html')