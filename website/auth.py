from flask import jsonify
import json

from .app import app
from .models import User


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
        
    return jsonify(json.dumps(users_dict))

@app.route('/get_user/<uid>', methods=['GET'])
def get_user_by_id(uid):
    user = User.query.filter_by( id = uid ).first()
    user_dict = {}
    if user:
        user_dict['id'] = user.id
        user_dict['username'] = user.username
        user_dict['full_name'] = user.full_name
        user_dict["email"] = user.email
    
    return jsonify(json.dumps(user_dict))
    
    # return users