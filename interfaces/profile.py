#
# list.py : Interfaces to access list.
#

from db import profile
from db import user
from interfaces import app
from flask import request
from flask import session
import json

# /profile/rate/<ingredient> : Rate an ingredient in the user's profile
@app.route("/profile/rate/ingredient", methods=["POST","GET"])
def rate_ingredient():
    """ Interface /profile/rate/ingredient
        Rate an ingredient in the user's profile """
    
    # Session informations
    username = session["username"]
    password = session["password"]

    # Check login
    cond, msg = user.check_login(username, password)
    if not cond:
        return json.dumps({"response" : -1, "message" : msg})

    # Get ingredient's name and rating
    ingredient = request.form["ingredient"]
    rating = int(request.form["rating"])

    # Check ingredient
    if type(ingredient) != unicode:
        return json.dumps({"response" : -1, "message" : "Ingredient should be a string"})

    # Check rating
    if type(rating) != int:
        return json.dumps({"response": -1, "message": "Rating must be integer"})

    # Check rating range
    if rating > 5 or rating < -1:
        return json.dumps({"response": -1, "message": "Rating must be between -1 and 5"})

    # Rate the ingredient
    profile.rate_ingredient(username, ingredient, rating)
    
    # OK
    return json.dumps({"response" : 0, "message" : "OK"})

# /profile : Get the user's profile
@app.route("/profile", methods=["POST","GET"])
def get_profile():
    """ Interface /profile
        Get the user's profile. """

    # Session informations
    username = session["username"]
    password = session["password"]
    print "Username : ", username
    # Check login
    cond, msg = user.check_login(username, password)
    if not cond:
        return json.dumps({"response": -1, "message": msg})

    # Get all the ingredient rating
    rates = profile.get_user_profile(username)

    # For each rates
    results = []
    for rate in rates:
        results += [{"ingredient" : rate[1], "rating" : rate[2]}]

    # Return results
    return json.dumps({"response" : 0, "message" : "OK", "count" : len(results), "results" : results})