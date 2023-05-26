from flask import request, render_template
from .app import app

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        print('got post')
        return "POST!"
    
    return render_template("register.html")

@app.route('/logout')
def logout():
    return "Logout on BETA"