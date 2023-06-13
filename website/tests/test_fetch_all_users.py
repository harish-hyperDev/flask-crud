import json, requests
from website.app import app


class TestFetchUsers:
    
    """
    TEST for checking error STATUS CODE on Request
    WHEN fetching users WITHOUT providing AUTH TOKEN
    """
    def test_error_status_code_when_fetching_users_without_token(self):
        
        url = "http://localhost:5000/get-users"
        
        response = requests.get(url = url)
        assert response.status_code == 401
        
    
    """
    TEST for checking error STATUS CODE on Request
    WHEN fetching users WITH a RANDOM AUTH TOKEN
    """
    def test_error_status_code_when_fetching_users_with_random_token(self):
        
        url = "http://localhost:5000/get-users"
        headers = {'Authorization': 'Bearer random123'}
        
        response = requests.get(url = url, headers = headers)
        assert response.status_code == 401
        
    
    """
    TEST for checking error STATUS CODE on Request
    WHEN fetching users WITH correct AUTH TOKEN
    """
    def test_fetch_users_with_token(self):
        AUTH_TOKEN = app.config['SECRET_KEY']
        
        url = "http://localhost:5000/get-users"
        headers = {'Authorization': 'Bearer ' + AUTH_TOKEN}
        
        response = requests.get(url = url, headers = headers)
        assert response.status_code == 200
        
    