#
# list.py : Interfaces to access recipes.
#

from interfaces import app
import json
from query import Ingredients
from query import OpenFood


def get_ingredients(queryrequest):
    ingredientobject = OpenFood(queryrequest)
    ingredients = Ingredients(ingredientobject)
    return ingredients.get_meals()