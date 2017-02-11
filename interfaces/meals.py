#
# meals.py : Interface to access meals.
#

from interfaces import app
import json
from query import Meals
from query import Food2forkMeal
from flask import request

# /recipe/list: to get the list of meals
@app.route("/recipe/list", methods=["GET"])
def get_meals():
    """
    Requires POST request with fields::

        "constraints" : the constraints (e.g., vegan, italian, etc.) separated by commas
        "nummeals" :  number of meals to return

    :return: JSON of meals. For each "meal_id" it has "title" and "image_url".
    """

    # Get the constraints from the POST request
    constraints = request.args.get("constraints")
    # Get the number of meals
    number_of_meals = request.args.get("nummeals")

    # create meal object for the specific API querying
    foodobject = Food2forkMeal(constraints)
    # static wrapper for meal objects
    meals_selector = Meals.instance()
    meals_selector.set_query_object(foodobject)
    # get the meals given the number
    returned_meals = meals_selector.get_meals(number_of_meals)
    if returned_meals:
        return json.dumps({"response": 0, "message": "OK", "results": returned_meals})
    else:
        return json.dumps({"response": -1, "message": "Error: no meals were found"})
