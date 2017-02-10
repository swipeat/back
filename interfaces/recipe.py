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
    # Get the the meal Ids that were selected by user from the POST request
    meal_ids = request.form["mealsids"]

    ingredientobject = Food2forkIngredients(meal_ids)
    ingredients = Ingredients(ingredientobject)
    returned_ingredients = ingredients.get_ingredients()

    if returned_ingredients:
        return json.dumps({"response": 0, "message": "OK", "results": returned_ingredients})
    else:
        return json.dumps({"response": -1, "message": "Error: no meals were found"})
