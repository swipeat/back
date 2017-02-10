#
# meals.py : Interface to access meals.
#

from interfaces import app
import json
from query import Meals
from query import Food2fork


def get_meals(queryrequest, number=5):
    foodobject = Food2fork(queryrequest)
    meals = Meals(foodobject)
    return meals.get_meals(number)