from flask import jsonify
import json

from .app import app
from .models import User

# route for returning all users in JSON format

@app.route('/get-users', methods=['GET'])
def get_users():
    
    # GET all users FROM DATABASE
    users = User.query.all()
    users_list = []
    
    # APPEND all users in list
    for user in users:
        d = {}
        d["id"] = user.id
        d["username"] = user.username
        d["full_name"] = user.full_name
        d["email"] = user.email
        
        users_list.append(d)
    
    # return users in JSON format
    return jsonify(json.dumps(users_list))


# route for returning a single user based on 'User ID(uid)' in JSON format

@app.route('/get-user/<uid>', methods=['GET'])
def get_user_by_id(uid):
    
    # FIND user by 'id'
    user = User.query.filter_by( id = uid ).first()
    
    # STORE the user in dict format (later parsed as JSON)
    user_dict = {}
    if user:
        user_dict['id'] = user.id
        user_dict['username'] = user.username
        user_dict['full_name'] = user.full_name
        user_dict["email"] = user.email

    # RETURN the found user by 'id' in JSON format
    return jsonify(json.dumps(user_dict))
    
    # return users