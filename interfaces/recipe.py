#
# list.py : Interfaces to access recipes.
#

from interfaces import app
import json
from query import Ingredients
from query import Food2forkIngredients
from flask import request


@app.route("/list/get", methods=["POST"])
def get_ingredients():
    # Get the the dish Ids that were selected by user from the POST request
    dish_ids = request.form["dishesids"].split(",")
    # create dish object for the specific API querying
    ingredientobject = Food2forkIngredients(dish_ids)
    # static wrapper for dish objects
    ingredient_selector = Ingredients.instance()
    ingredient_selector.set_query_object(ingredientobject)
    # get the dishes given the number
    returned_ingredients = ingredient_selector.get_ingredients()

    if returned_ingredients:
        return json.dumps({"response": 0, "message": "OK", "results": returned_ingredients})
    else:
        return json.dumps({"response": -1, "message": "Error: no dishes were found"})
