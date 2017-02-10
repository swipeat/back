
import sqlite3
from tinydb import TinyDB, where

# Check if account exists
def account_exists(username):

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Query
    c.execute('''SELECT * FROM swipeat_accounts WHERE username like \'''' + username + "'")
    all_rows = c.fetchall()

    # Check if exists
    if len(all_rows) == 0:
        return False
    else:
        return True

# Create an account
def create_account(username, password):

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # If account exists => exit
    if account_exists(username):
        return False, "Account already exists"
    else:
        c.execute('''INSERT INTO swipeat_accounts(username, password) VALUES(:username,:password)''', {'username' : username, 'password' : password})
        conn.commit()
        return True, "Account created"

# Check login and password
def check_login(username, password):

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # No account?
    if not account_exists(username):
        return False, "Username does not exists"
    else:
        # Get info
        c.execute('''SELECT * FROM swipeat_accounts WHERE username like \'''' + username + "'")
        row = c.fetchone()
        if row[1] == password:
            return True, "Login succeeded"
        else:
            return False, "Wrong password"