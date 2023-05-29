from flask import request, render_template

from .app import app
from .models import UserAccount

@app.route('/login')
def login():
    return render_template("login.html")


# need to add validations
def validations(form_dict):
    errors_list = []
    errors_dict = {}
    print("errors dict : ", form_dict)
    
    for key in form_dict.keys():
        print("password : ", form_dict['password'])
        if form_dict['password'] != form_dict['confirm_password']:
            errors_dict['confirm_password'] = "Passwords do not match!"
        if form_dict[key].strip() == "":
            errors_dict[key] = "This above field is invalid!"
    
    return errors_dict


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        
        register_fields = request.form.to_dict()
        errors = validations(register_fields)
        
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
            print("User has been successfully registered!")
    
    return render_template("register.html")


@app.route('/logout')
def logout():
    return "Logout on BETA"