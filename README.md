## FLASK CRUD App

##### This app is a CRUD App(Create, Read, Update, Delete) created with Flask micro-framework.

#### This app does the following

1. Create new user
2. View all the existing user(s)
3. Edit existing user
4. Delete existing user

#### All the above options are accessible from http://localhost:5000/

#### URLS for fetching data
1. All the users can be viewed in JSON format with the URL: http://localhost:5000/get-users
2. A specifice user by id can be viewed in JSON format with the URL: http://localhost:5000/get-user/:user-id

The app can be run with the command

    python3 main.py

The tests for this app are written with **pytest**
The tests are advised to be run with the command

    python3 -m pytest -vv -s website/tests/test_*.py