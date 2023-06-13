from website.app import db
from website.models import User

import pytest


class TestDeleteUser:
    
    @pytest.fixture(scope='module')
    def delete_user_id(self):
        return 'test-id-1'
    
    
    def test_delete_user_and_save_to_db(self, delete_user_id):
        
        # GET user by 'id'
        found_user = User.query.filter_by(id=delete_user_id)
        
        """
        IF user found BY id
            DELETE user
            COMMIT changes to DATABASE
        
        ELSE
            FAIL test
        """
        if found_user.first() is not None:
            found_user.delete()
            db.session.commit()
        else:
            assert False, 'Reason: User not found by ID'
        
        deleted_user = User.query.filter_by(id=delete_user_id).first()
        if deleted_user is None:
            assert True
        else:
            assert False

