from website.app import db
from website.models import User

import pytest


class TestDeleteUser:
    
    @pytest.fixture(scope='module')
    def delete_user_id(self):
        return 'ec12e487062d44dcbd4d13487c52afe8'
    
    
    def test_delete_user_and_save_to_db(self, delete_user_id):
        # delete user by id
        User.query.filter_by(id=delete_user_id).delete()
        db.session.commit()
        
        deleted_user = User.query.filter_by(id=delete_user_id).first()
        print(deleted_user)
        
        assert deleted_user == None

