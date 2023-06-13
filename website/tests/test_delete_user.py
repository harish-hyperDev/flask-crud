from website.app import db
from website.models import User

import pytest


class TestDeleteUser:
    
    @pytest.fixture(scope='module')
    def delete_user_id(self):
        return 'ecdf1ca12d9c4ddd888e3186f5c8b8a3'
    
    
    def test_delete_user_and_save_to_db(self, delete_user_id):
        # delete user by id
        User.query.filter_by(id=delete_user_id).delete()
        db.session.commit()
        
        deleted_user = User.query.filter_by(id=delete_user_id).first()
        
        assert deleted_user == None

