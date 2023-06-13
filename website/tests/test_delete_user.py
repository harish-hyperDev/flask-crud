from website.app import db
from website.views import edit_user_validations
from flask_uuid import uuid
from website.models import User

import pytest


class TestEditUser:
    
    @pytest.fixture(scope='module')
    def edit_user_id(self):
        return 'ec12e487062d44dcbd4d13487c52afe8'
    
    @pytest.fixture(scope='module')
    def form_data_fail(self):
        
        d = {"full_name": "test5",
             "password": "test123",
             "confirm_password": "test123"
            }
        
        return d
    
    @pytest.mark.dependency()
    def test_form_data_validations(self, form_data_fail):
        # check validations
        form_data = form_data_fail
        errors = edit_user_validations(form_data)
        
        if errors:
            errors_str = ', '.join(x for x in errors.keys())
            e = 'Reason: Error(s) caught during validating - ' + errors_str
            assert False, e
            
        else:
            assert True
    
    @pytest.mark.dependency(depends = ['TestEditUser::test_form_data_validations'])
    def test_edit_user_and_save_to_db(self, edit_user_id, form_data_fail):
        # get id of user
        edit_user_data = User.query.filter_by(id=edit_user_id).first()
        form_data = form_data_fail

        if edit_user_data:
            edit_user_data.full_name = form_data['full_name']
            edit_user_data.password = form_data['password']

            db.session.commit()
            
            after_edit = User.query.filter_by(id=edit_user_id).first()
            
            assert after_edit.full_name == form_data['full_name']
            assert after_edit.password == form_data['password']
            

