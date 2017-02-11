#
# list.py : Interfaces to access recipes.
#

from interfaces import app
import json
from query import Ingredients
from query import Food2forkIngredients
from flask import request
# from flask import session
# from db import user

# /recipe/info: # get the detailed info of a recipe
@app.route("/recipe/info", methods=["GET"])
def get_ingredients():
    """
    Get the detailed info of a recipe
    :return: A JSON of the recipe
    """

    # # Session informations
    # username = session["username"]
    # password = session["password"]
    #
    # # Check login
    # cond, msg = user.check_login(username, password)
    # if not cond:
    #     return json.dumps({"response": -1, "message": msg})

    # Get the the meal Ids that were selected by user from the request
    meal_ids = request.args.get("mealsids").split(",")

    # Create meal object for the specific API querying
    ingredientobject = Food2forkIngredients(meal_ids)

    # Static wrapper for meal objects
    ingredient_selector = Ingredients.instance()
    ingredient_selector.set_query_object(ingredientobject)

    # Get the ingredients
    returned_ingredients = ingredient_selector.get_ingredients()

    # If list ok, send the results
    if returned_ingredients:
        return json.dumps({"response": 0, "message": "OK", "results": returned_ingredients})
    else:
        return json.dumps({"response": -1, "message": "Error: no dishes were found"})