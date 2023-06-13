from flask import jsonify, request
from functools import wraps

import json

from .app import app
from .models import User


JWT_SECRET = app.config['SECRET_KEY']

# return all users in JSON format
def get_all_users():
    users = []
                
    for user in User.query.all():
        d = {}
        d["id"] = user.id
        d["username"] = user.username
        d["full_name"] = user.full_name
        d["email"] = user.email

        users.append(d)
    
    return users

"""
Function for verifying the JWT Token and return data
"""
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Authentication Token is missing!'})
       
        payload = None
        
        '''
        Checking token
        '''
        if token == JWT_SECRET:
            payload = get_all_users()
            
            # data = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
            # print("data - ", jwt.decode(data, token, algorithms=["HS256"]))
            
        else:
            return jsonify({'message': "Token is invalid"})
 
        return f(payload, *args, **kwargs)
    return decorator


# route for returning all users in JSON format

@app.route('/get-users', methods=['GET'])
@token_required
def get_users(users):
    # return users in JSON format
    return jsonify(json.dumps(users))


@app.route('/test', methods=['GET'])
@token_required
def test(tk):
    return tk
    # return jsonify({'message': 'hello'})