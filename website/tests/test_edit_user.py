from website.app import app, db
from website.views import edit_user_validations
from flask_uuid import uuid
from website.models import User

import pytest, time


class TestEditUser:
    
    @pytest.fixture(scope='module')
    def edit_user_id(self):
        return 'ec12e487062d44dcbd4d13487c52afe8'
    
    @pytest.mark.dependency()
    def test_edit_user_validations(self, edit_user_id):
        
        # check validations
        form_data = request.form.to_dict()
        print(form_data)
        errors = edit_user_validations(form_data)
        print(errors)
    
    @pytest.mark.dependency(depends = ['TestEditUser::hello'])
    def test_edit_user(self, edit_user_id):
        # get id of user
        edit_user_data = User.query.filter_by(id=edit_user_id).first()

       

        # if errors assert None
            
        # else assert True
        edit_user_data.full_name = form_data['full_name']
        edit_user_data.password = form_data['password']
        edit_user_data.confirm_password = form_data['confirm_password']

        db.session.commit()

