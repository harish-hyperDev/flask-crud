from flask import render_template, session, request, redirect, url_for
from flask_uuid import uuid

import time

from .models import User
from .app import app, db


# route for listing users page
@app.route('/', methods=['GET', 'POST'])
def admin_home():
    if request.method == "POST":
        
        '''
        Delete the user if the request.form contains "delete_id" and save changes to database
        '''
        if 'delete_id' in request.form.to_dict().keys():
            userid_to_delete = request.form.to_dict()['delete_id']
            User.query.filter_by(id=userid_to_delete).delete()
            db.session.commit()
        
        '''
        Edit the user if the request.form contains "edit_id" based on the id of selected user
        '''
        if 'edit_id' in request.form.to_dict().keys():
            userid_to_edit = request.form.to_dict()['edit_id']
            session['edit_id'] = userid_to_edit
            
            return redirect(url_for('edit_user', edit_id = userid_to_edit))
        
            
        return render_template('/home.html')
        
    else:
        return render_template('/home.html')


# route for adding new user(s)
@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        
        register_fields = request.form.to_dict()
        errors = validations(register_fields)
        
        if errors:
            return render_template('add_user.html', errors = errors, form_data = register_fields)
        
        else:
            user = User(
                        id = uuid.uuid4().hex,      # for generating unique user id
                        full_name = register_fields['full_name'],
                        username = register_fields['username'],
                        email = register_fields['email_id'],
                        password = register_fields['password']
                    )
            
            db.session.add(user)
            db.session.commit()
            
            time.sleep(3)
            return redirect(url_for('admin_home'))
    
    return render_template("add_user.html")


# route for editing existing user(s)
@app.route('/edit-user', methods=['GET', 'POST'])
def edit_user():
    edit_id = request.args.get('edit_id')
    edit_user_data = User.query.filter_by(id=edit_id).first()
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        errors = edit_user_validations(form_data)
        
        if errors:
            return render_template('edit_user.html', 
                                    full_name = form_data['full_name'],
                                    username = edit_user_data.username,
                                    email_id = edit_user_data.email,
                                    password = form_data['password'],
                                    confirm_password = form_data['confirm_password'],
                                    errors = errors)
        else:
            edit_user_data.full_name = form_data['full_name']
            edit_user_data.password = form_data['password']
            edit_user_data.confirm_password = form_data['confirm_password']
            
            db.session.commit()
            time.sleep(2)
            return redirect(url_for('admin_home'))
    
    else:
        return render_template('edit_user.html', 
                                full_name = edit_user_data.full_name,
                                username = edit_user_data.username,
                                email_id = edit_user_data.email)
        

# validations to be perfromed on creating new User
def validations(form_dict):
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


def edit_user_validations(form_dict):
    errors_dict = {}

    for key in form_dict.keys():
        if form_dict['password'] != form_dict['confirm_password']:
            errors_dict['confirm_password'] = "Password mismatch!"
            
        if form_dict[key].strip() == "":
            errors_dict[key] = "This above field is invalid!"
            
    return errors_dict


