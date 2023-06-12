from website.app import app, db
from website.views import validations
from flask_uuid import uuid
from website.models import User

import pytest, time

class TestAddUser:
    
    @pytest.fixture(scope='module')
    def temp_user(self):
        temp_user_data = {  "full_name": "test2",
                            "username": "testuser2",
                            "email_id": "test2@alohatechnology.com",
                            "password": "test123",
                            "confirm_password": "test123"
                        }
        return temp_user_data
    
    
    @pytest.mark.dependency()
    def test_validations(self, temp_user):
        errors = validations(temp_user)
        
        if errors:
            errors_str = ', '.join(x for x in errors.keys())
            e = 'Reason: Error(s) caught on validating - ' + errors_str
            assert False, e
                
        else:
            assert True
        
    
    @pytest.mark.dependency(depends=['TestAddUser::test_validations'])
    def test_add_user(self, temp_user):
        
        user = User(
                id = uuid.uuid4().hex,      # for unique user id
                full_name = temp_user['full_name'],
                username = temp_user['username'],
                email = temp_user['email_id'],
                password = temp_user['password']
            )
        
        db.session.add(user)
        db.session.commit()
        
        user_created = User.query.filter_by(email = temp_user['email_id'])
        
        if user_created:
            assert True
        else:
            assert False, "Reason: Error caught while creating new User"

# t = TestAddUser()