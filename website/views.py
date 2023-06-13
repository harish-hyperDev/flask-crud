from flask import render_template, request, redirect, url_for
from flask_uuid import uuid

import time

from .models import User
from .app import app, db


# route for listing users page(table)

@app.route('/', methods=['GET', 'POST'])
def admin_home():
    
    AUTH_HEADER = app.config['SECRET_KEY']
    if request.method == "POST":
        
        '''
        IF the request.form(data from input fields) CONTAINS "delete_id" 
        DELETE user by "id"
        COMMIT changes to DATABASE
        '''
        if 'delete_id' in request.form.to_dict().keys():
            userid_to_delete = request.form.to_dict()['delete_id']
            User.query.filter_by(id=userid_to_delete).delete()
            db.session.commit()
        
        '''
        IF the request.form(data from input fields) CONTAINS "edit_id"
        RETURN template FOR editing user
        '''
        if 'edit_id' in request.form.to_dict().keys():
            userid_to_edit = request.form.to_dict()['edit_id']
            
            return redirect(url_for('edit_user', edit_id = userid_to_edit))
        
        # SENDING AUTH TOKEN to home template for fetching data from API
        return render_template('/home.html', token=AUTH_HEADER)
        
    else:
        # SENDING AUTH TOKEN to home template for fetching data from API
        return render_template('/home.html', token=AUTH_HEADER)


# route for adding new user(s)

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        
        register_fields = request.form.to_dict()
        
        # perform validations on data extracted from input fields
        errors = validations(register_fields)
        
        """
        IF errors are FOUND
        RETURN 'add user' template with error messages AND form data
        
        ELSE create user by the data extracted FROM input fields
        COMMIT changes to DATABASE
        REDIRECT back to home page
        """
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


# route for editing user(s)

@app.route('/edit-user', methods=['GET', 'POST'])
def edit_user():
    
    # get 'id' of the user to edit
    edit_id = request.args.get('edit_id')
    
    # find the user object by 'id'
    edit_user_data = User.query.filter_by(id=edit_id).first()
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        errors = edit_user_validations(form_data)
        
        """
        IF errors are FOUND
        RETURN 'edit user' template with error messages AND form data
        
        ELSE edit user by the data extracted FROM input fields
        AND COMMIT changes to DATABASE
        AND REDIRECT back to home page
        """
        if errors:
            return render_template('edit_user.html', 
                                    errors = errors,
                                    full_name = form_data['full_name'],
                                    username = edit_user_data.username,
                                    email_id = edit_user_data.email,
                                    password = form_data['password'],
                                    confirm_password = form_data['confirm_password'])
            
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
        
        # Create error message if password and confirm password are NOT same 
        if form_dict['password'] != form_dict['confirm_password']:
            errors_dict['confirm_password'] = "Password mismatch!"
            
        # Create error message if any input field is empty
        if form_dict[key].strip() == "":
            errors_dict[key] = "This above field is invalid!"
    
    # Create error message if given EMAIL ADDRESS is already existing in DATABASE
    if email_exists:
        errors_dict['email_id'] = "This email address has already been used!"
    
    # Create error message if given USERNAME is already existing in DATABASE
    if uname_exists:
        errors_dict['username'] = "The given username is already taken!"
    
    return errors_dict


# validations to be perfromed while editing User

def edit_user_validations(form_dict):
    errors_dict = {}

    for key in form_dict.keys():
        
        # Create error message if password and confirm password are NOT same 
        if form_dict['password'] != form_dict['confirm_password']:
            errors_dict['confirm_password'] = "Password mismatch!"
            
        # Create error message if ANY input field is empty
        if form_dict[key].strip() == "":
            errors_dict[key] = "This above field is invalid!"
            
    return errors_dict


