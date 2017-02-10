#!/usr/bin/env python2.7
#
# Swipeat project main file.
#

# Imports all interfaces
from interfaces import app
from query import Meals
from query import Ingredients

# Launch the REST server
if __name__ == "__main__":
    # init static wrappers
    Meals.create()
    Ingredients.create()

    """ Launch the REST server """
    app.run(host='0.0.0.0', port=80)
