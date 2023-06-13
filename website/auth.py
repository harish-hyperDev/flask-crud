from flask import jsonify, request
from functools import wraps

from .app import app
from .models import User


AUTH_SECRET = app.config['SECRET_KEY']

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
Function for verifying the Auth Token and return data
"""
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401
       
        payload = None
        
        '''
        Checking token 
        '''
        if token == AUTH_SECRET:
            payload = get_all_users()
            
        else:
            return jsonify({'error': "Token is invalid"}), 401
 
        '''
        RETURN 'payload' TO get_users function AS parameter 'users'
        '''
        return f(payload, *args, **kwargs)
    return decorator


# route for returning all users in JSON format

@app.route('/get-users', methods=['GET'])
@token_required
def get_users(users):
    # return users in JSON format
    return jsonify(users), 200
