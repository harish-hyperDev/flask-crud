from website.app import db
from website.views import edit_user_validations
from website.models import User

import pytest


class TestEditUser:
    
    @pytest.fixture(scope='module')
    def edit_user_id(self):
        return 'test-id-1'
    
    @pytest.fixture(scope='module')
    def form_data(self):
        
        d = {"full_name": "test1 edited",
             "password": "testing123",
             "confirm_password": "testing123"
            }
        
        return d
    
    @pytest.mark.dependency()
    def test_form_data_validations(self, form_data):
        # check validations
        errors = edit_user_validations(form_data)
        
        if errors:
            errors_str = ', '.join(x for x in errors.keys())
            e = 'Reason: Error(s) caught during validating - ' + errors_str
            assert False, e
            
        else:
            assert True
    
        """
        RUN below test only after validations have been succeeded
        """
    @pytest.mark.dependency(depends = ['TestEditUser::test_form_data_validations'])
    def test_edit_user_and_save_to_db(self, edit_user_id, form_data):
        
        # get user by 'id'
        edit_user_data = User.query.filter_by(id=edit_user_id).first()

        """
        IF user has been found BY id
            EDIT user data
            COMMIT changes to DATABASE
            ASSERT IF changes are SAME as GIVEN data from input fields
        
        ELSE
            FAIL Test
        """
        if edit_user_data:
            edit_user_data.full_name = form_data['full_name']
            edit_user_data.password = form_data['password']

            db.session.commit()
            
            after_edit = User.query.filter_by(id=edit_user_id).first()
            
            assert after_edit.full_name == form_data['full_name']
            assert after_edit.password == form_data['password']
            
        else:
            assert False, 'Reason: User not found by ID'

