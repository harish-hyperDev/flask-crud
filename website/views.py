from flask import render_template, session, request
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy

from .models import AdminAccount, UserAccount
from .app import app, db, toastr

# from flask import Blueprint

# views = Blueprint('views', __name__)

@app.route('/')
def index():
    return  render_template('base.html')

@app.route('/home')
@login_required
def home():
    # flash("All OK", 'success')
    # print("current user : ", current_user.username)
    return render_template('user/home.html')

# route for admin home page
@app.route('/admin/home', methods=['GET', 'POST'])
@login_required
def admin_home():
    if AdminAccount.query.get(current_user.id):
        if request.method == "POST":
            
            userid_to_delete = request.form.to_dict()['id']
            UserAccount.query.filter_by(id=userid_to_delete).delete()
            print("here")
            db.session.commit()
                
            return render_template('admin/home.html')
            
        else:
            return render_template('admin/home.html')

