from flask import render_template, session, request, redirect, url_for
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
            if 'delete_id' in request.form.to_dict().keys():
                userid_to_delete = request.form.to_dict()['delete_id']
                UserAccount.query.filter_by(id=userid_to_delete).delete()
                print("here")
                db.session.commit()
                
            if 'edit_id' in request.form.to_dict().keys():
                userid_to_edit = request.form.to_dict()['edit_id']
                session['edit_id'] = userid_to_edit
                
                return redirect(url_for('edit-user'))
            
                
            return render_template('admin/home.html')
            
        else:
            return render_template('admin/home.html')
    else:
        return "<h3>You're not authenticated to view this page!</h3>"

@app.route('/edit-user', methods=['GET', 'POST'])
def edit_user():
    return render_template('admin/edit_user.html')
