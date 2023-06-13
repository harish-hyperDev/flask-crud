from website.app import db
from website.views import validations
from flask_uuid import uuid
from website.models import User

import pytest

class TestAddUser:
    
    @pytest.fixture(scope='module')
    def temp_user(self):
        temp_user_data = {  "full_name": "test1",
                            "username": "testuser1",
                            "email_id": "test1@alohatechnology.com",
                            "password": "test123",
                            "confirm_password": "test123"
                        }
        return temp_user_data
    
    # GET data for creating user from 'temp_user'
    @pytest.mark.dependency()
    def test_form_data_validations(self, temp_user):
        
        """
        CHECK FOR errors on validations
        IF errors FOUND
            FAIL Test
        ELSE
            PASS Test
        """
        errors = validations(temp_user)
        
        if errors:
            errors_str = ', '.join(x for x in errors.keys())
            e = 'Reason: Error(s) caught on validating - ' + errors_str
            assert False, e
                
        else:
            assert True
        
        """
        RUN below test only after validations are successful
        
        """
    @pytest.mark.dependency(depends=['TestAddUser::test_form_data_validations'])
    def test_add_new_user_to_db(self, temp_user):
        
        """
        CREATE USER
        COMMIT changes to DATABASE
        """
        user = User(
                id = "test-id-1",      # the same id is given in tests for edit_user and delete_user
                full_name = temp_user['full_name'],
                username = temp_user['username'],
                email = temp_user['email_id'],
                password = temp_user['password']
            )
        
        # COMMITTING changes to DATABASE
        db.session.add(user)
        db.session.commit()
        
        """
        IF created user data is SAME as GIVEN data from form data
            PASS Test
            
        ELSE
            FAIL Test
        """
        user_created = User.query.filter_by(email = temp_user['email_id'])
        
        if user_created:
            assert True
        else:
            assert False, "Reason: Error caught while creating new User"

# t = TestAddUser()