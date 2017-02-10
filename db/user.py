
from tinydb import TinyDB, where

# Create an account
def create_account(username, password):

    # TinyDB
    db = TinyDB('db.json')

    # Users table
    users_table = db.table("users") 

    # Check if the account already exists
    if len(users_table.search(username == username)) != 0:
        return False, "User already exists"

    # Insert account
    users_table.insert({'username' : username, 'password' : password})

    return True, "Account created"

# Check login and password
def check_login(username, password):

    # TinyDB
    db = TinyDB('/path/to/db.json')

    # Users table
    users_table = db.table("users") 

    # Get username's informations
    account_info = users_table.search(username == username)

    # Check if we found insert
    if len(account_info) < 1:
        return False, "Unknown username"
    else:
        if account_info[0]["password"] != password:
            return False, "Incorrect password"
    return True, "Login success"