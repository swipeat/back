# Init file to import all the interfaces functions

# Import
from flask import Flask

# Flask app settings
app = Flask(__name__)
app.debug = True

# Import interfaces
import interfaces.list
import interfaces.recipe
import interfaces.login
import interfaces.dishess
