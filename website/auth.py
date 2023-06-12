from flask import request, render_template, redirect, url_for, jsonify, session
from flask_uuid import uuid

from .app import app, db
from .models import User

import time

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_dict = []
    
    for user in users:
        d = {}
        d["id"] = user.id
        d["username"] = user.username
        d["full_name"] = user.full_name
        d["email"] = user.email
        
        users_dict.append(d)
        
        
    import json
    return jsonify(json.dumps(users_dict))
    
    # return users