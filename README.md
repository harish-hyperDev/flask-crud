## FLASK CRUD App

##### This app is a CRUD App(Create, Read, Update, Delete) created with Flask micro-framework.

#### This app does the following

1. Create new user
2. View all the existing user(s)
3. Edit existing user
4. Delete existing user

#### All the above options are accessible from http://localhost:5000/

#### URL for fetching data
 - All the users can be viewed in JSON format with the URL: http://localhost:5000/get-users (protected with Authentication Bearer Token)

The app can be run with the command

    python3 main.py

The tests for this app are written with **pytest**
The tests are advised to be run with the command

    python3 -m pytest -vv website/tests/<test_name>.py