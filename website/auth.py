from flask import request, render_template
from .app import app

@app.route('/login')
def login():
    return render_template("login.html")

# need to add validations
def validations():
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    errors = {}
    if request.method == "POST":
        print("GOT POST")
        # full_name = request.form.get
        print("Full name is : ", request.form.get('full_name'))
        errors['full_name'] = "Full Name"
        
        if errors:
            return render_template('register.html', errors = errors)
    
    return render_template("register.html")

@app.route('/logout')
def logout():
    return "Logout on BETA"