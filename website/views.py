from flask import render_template, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_uuid import uuid

import time

from .models import User
from .app import app, db

# route for admin home page
@app.route('/', methods=['GET', 'POST'])
def admin_home():
    if request.method == "POST":
        if 'delete_id' in request.form.to_dict().keys():
            userid_to_delete = request.form.to_dict()['delete_id']
            User.query.filter_by(id=userid_to_delete).delete()
            print("here")
            db.session.commit()
            
        if 'edit_id' in request.form.to_dict().keys():
            print(request.form.to_dict()['edit_id'])
            userid_to_edit = request.form.to_dict()['edit_id']
            session['edit_id'] = userid_to_edit
            
            return redirect(url_for('edit_user', edit_id = userid_to_edit))
        
            
        return render_template('/home.html')
        
    else:
        return render_template('/home.html')



# need to add validations
def validations(form_dict):
    errors_list = []
    errors_dict = {}
    
    email_exists = User.query.filter_by(email = form_dict['email_id']).first()
    uname_exists = User.query.filter_by(username = form_dict['username']).first()
    
    
    for key in form_dict.keys():
        if form_dict['password'] != form_dict['confirm_password']:
            errors_dict['confirm_password'] = "Password mismatch!"
        if form_dict[key].strip() == "":
            errors_dict[key] = "This above field is invalid!"
    
    if email_exists:
        errors_dict['email_id'] = "This email address has already been used!"
        
    if uname_exists:
        errors_dict['username'] = "The given username is already taken!"
    
    return errors_dict


def form_to_dict(form_data):
    return form_data.to_dict()


@app.route('/add-user', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        
        register_fields = form_to_dict(request.form)
        errors = validations(register_fields)
        
        if errors:
            return render_template('add_user.html', errors = errors, form_data = register_fields)
        
        else:
            user = User(
                        id = uuid.uuid4().hex,      # for unique user id
                        full_name = register_fields['full_name'],
                        username = register_fields['username'],
                        email = register_fields['email_id'],
                        password = register_fields['password']
                    )
            
            # user.save()
            db.session.add(user)
            db.session.commit()
            
            time.sleep(3)
            return redirect(url_for('home'))
    
    return render_template("add_user.html")



@app.route('/edit-user', methods=['GET', 'POST'])
def edit_user():
    print('editing begins')
    edit_id = request.args.get('edit_id')
    edit_user_data = User.query.filter_by(id=edit_id).first()
    print(edit_user_data)
    return render_template('admin/edit_user.html', full_name = edit_user_data.full_name)
