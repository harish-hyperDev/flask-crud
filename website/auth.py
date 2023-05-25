from .app import app

@app.route('/login')
def login():
    return "<p>Login</p>"

@app.route('/logout')
def logout():
    return "<p>Logout</p>"