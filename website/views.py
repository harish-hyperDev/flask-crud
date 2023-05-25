from flask import render_template
from .app import app
# from flask import Blueprint

# views = Blueprint('views', __name__)

@app.route('/')
def index():
    return  render_template('base.html')

