#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Nils Schaetti <n.schaetti@gmail.com>
# @date: Fri 10 Feb

from interfaces import app
from db import list
from db import user
import json
from flask import request
from query import Ingredients
from query import Food2forkIngredients
from flask import session

# /list/get : Get the current list
@app.route("/list/get")
def get_user_list():
    """
    Get the complete list of the user with all the current ingredients
    :return: A JSON string with the current list of ingredients.
    """

    # Session informations
    username = session["username"]
    password = session["password"]

    # Check login
    cond, msg = user.check_login(username, password)
    if not cond:
        return json.dumps({"response": -1, "message": msg})

    # Get data
    rows = list.get_list(username)

    # For each rows
    results = []
    for row in rows:
        results += [row[1]]

    return json.dumps({"response": 0, "message": "Ok", "count": len(results), "results": results})

# /list/remove_ingredient : remove an ingredient from the list
@app.route("/list/remove_ingredient")
def remove_ingredient():
    """
    Remove an ingredient from the list
    :return:
    """

    # Session informations
    username = session["username"]
    password = session["password"]

    # Check login
    cond, msg = user.check_login(username, password)
    if not cond:
        return json.dumps({"response": -1, "message": msg})

    # Parameters
    ingredient = request.form["ingredient"]

    # Remove
    list.remove_ingredient(username, ingredient)

    return json.dumps({"response": 0, "message": "Ok"})


# /list/purge : Purge the list of ingredient
@app.route("/list/purge")
def purge_user_list():
    """
    Purge the user's list of ingredients
    :return: Confirmation
    """

    # Session informations
    username = session["username"]
    password = session["password"]

    # Check login
    cond, msg = user.check_login(username, password)
    if not cond:
        return json.dumps({"response": -1, "message": msg})

    # Remove
    list.purge_list(username)

    return json.dumps({"response": 0, "message": "OK"})

# /list/add_ingredient : Add an ingredient to the list
@app.route("/list/add_ingredient", methods=["POST"])
def add_ingredient():
    """
    Add an ingredient to the user's list
    :return: A JSON string confirmation for the client
    """

    # Session informations
    username = session["username"]
    password = session["password"]

    # Check login
    cond, msg = user.check_login(username, password)
    if not cond:
        return json.dumps({"response": -1, "message": msg})

    # Parameters
    ingredient = request.form["ingredient"]

    # Add the ingredient
    list.add_ingredient(username, ingredient)

    return json.dumps({"response": 0, "message": "OK"})

# /list/add_recipe : Add all ingredients of a recipe to the user's list
@app.route("/list/add_recipe", methods=["POST"])
def add_recipe():
    """
    Add all ingredients of a recipe to the user's list.
    :return: A JSON list of ingredients added.
    """

    # Session informations
    username = session["username"]
    password = session["password"]

    # Check login
    cond, msg = user.check_login(username, password)
    if not cond:
        return json.dumps({"response": -1, "message": msg})

    # Get the the meal Ids that were selected by user from the POST request
    meal_ids = request.form["mealsids"].split(",")

    # Create meal object for the specific API querying
    ingredientobject = Food2forkIngredients(meal_ids)

    # Static wrapper for meal objects
    ingredient_selector = Ingredients.instance()
    ingredient_selector.set_query_object(ingredientobject)

    # Get the meals given the number
    returned_ingredients = ingredient_selector.get_ingredients()

    # If ok
    if returned_ingredients:
        print returned_ingredients
        for ingredient in returned_ingredients["ingredients"]:
            # Add the ingredient
            list.add_ingredient(username, ingredient)
        return json.dumps({"response": 0, "message": "Ok", "results": returned_ingredients["ingredients"]})
    else:
        return json.dumps({"response": -1, "message": "Error: no meals were found"})