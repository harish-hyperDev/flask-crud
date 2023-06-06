from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user

from .app import app, db
from .models import UserAccount

import time


# need to add validations
def validations(form_dict):
    errors_list = []
    errors_dict = {}
    
    email_exists = UserAccount.query.filter_by(email = form_dict['email_id']).first()
    uname_exists = UserAccount.query.filter_by(username = form_dict['username']).first()
    
    
    for key in form_dict.keys():
        print("password : ", form_dict['password'])
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


def check_login(form_data):
    email_exists = UserAccount.query.filter_by(email = form_data['email_id']).first()
    login_errors = {}
    
    if email_exists:
        print("email  exists  pass: ", email_exists.password, " given pass : ", form_data['password'])
        if email_exists.password == form_data['password']:
            print("logged in ")
            login_user(email_exists)
            return True
        else:
            print("nahh")
            login_errors['password'] = "Invalid Password!"
            return login_errors
        
    else:
        login_errors['email_id'] = "Invalid Email Address!"
        login_errors['password'] = "Invalid Password!"
        
        return login_errors

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login_fields = form_to_dict(request.form)
        
        login_valid = check_login(login_fields)
        
        if login_valid == True:
            print("Login is valid")
            print(login_valid)
            return redirect(url_for('home'))
        else:
            return render_template('login.html', errors = login_valid, form_data = login_fields)
        
    
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        
        register_fields = form_to_dict(request.form)
        print(register_fields)
        errors = validations(register_fields)
        
        print(register_fields['email_id'])
        
        if errors:
            return render_template('register.html', errors = errors, form_data = register_fields)
        else:
            user = UserAccount(
                        full_name = register_fields['full_name'],
                        username = register_fields['username'],
                        email = register_fields['email_id'],
                        password = register_fields['password']
                    )
            
            # user.save()
            db.session.add(user)
            db.session.commit()
            print("User has been successfully registered!")
            
            flash("Account has been created!")
            flash("Redirecting back to login page.")
            # return render_template('register.html', errors = errors, form_data = register_fields)
            
            time.sleep(4)
            return redirect(url_for('login'))

    
    return render_template("register.html")

@app.route('/logout')
@login_required
def logout():
    return "Logout on BETA"