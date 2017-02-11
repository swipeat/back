#
# list.py : Interfaces to access list.
#

from db import user
from interfaces import app
import json
from flask import request
from flask import make_response
from flask import session

# /login : Login to user's account
@app.route("/login", methods=["POST"])
def login():
    """ Login to user's account """

    # Get login and password
    # login = request.authorization["username"]
    # password = request.authorization["password"]

    # temp hack to make demo faster
    login = "user"
    password = "user"

    # Do some check in the database
    cond, msg = user.check_login(login, password)
    if cond:
        # Set username/password in the response
        session["username"] = login
        session["password"] = password

        # Send ok response with cookie
        return json.dumps({"response" : 0, "message" : msg})
    else:
        # Sorry man
        return json.dumps({"reponse" : -1, "error" : "Wrong username or password"}, sort_keys=True)

# /login/signup : Create an account
@app.route("/login/signup", methods=["POST"])
def signup():
    """ Create a new account """

    # Get new username and password
    # username = request.form["username"]
    # password = request.form["password"]

    # temp hack to make demo faster
    username = "user"
    password = "user"

    # Try to create account
    resp, msg = user.create_account(username, password)

    # Create the account
    if resp:
        return json.dumps({"response" : 0, "message" : msg})
    else:
        return json.dumps({"response" : -1, "message" : msg})