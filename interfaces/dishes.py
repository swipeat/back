#
# dishes.py : Interface to access dishes.
#

from interfaces import app
import json
from query import Dishes
from query import Food2forkDish
from flask import request

# /recipe/getset: to get the list of dishes
@app.route("/recipe/getdishes", methods=["GET"])
def get_dishes():
    """
    Requires GET request with fields::

        "constraints" : the constraints (e.g., vegan, italian, etc.) separated by commas
        "numdishes" :  number of dishes to return

    :return: JSON of dishes. For each "dish_id" it has "title" and "image_url".
    """

    # Get the constraints from the GET request
    constraints = request.args.get("constraints").split(",")
    # Get the number of dishes
    number_of_dishes = request.args.get("numdishes")

    # create dish object for the specific API querying
    foodobject = Food2forkDish(constraints)
    # static wrapper for dish objects
    dishes_selector = Dishes.instance()
    dishes_selector.set_query_object(foodobject)
    # get the dishes given the number
    returned_dishes = dishes_selector.get_dishes(number_of_dishes)
    if returned_dishes:
        return json.dumps({"response": 0, "message": "OK", "results": returned_dishes})
    else:
        return json.dumps({"response": -1, "message": "Error: no dishes were found"})
