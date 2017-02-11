# Init file to import all the interfaces functions

# Import
from flask import Flask
from flask_cors import CORS, cross_origin

# Flask app settings
app = Flask(__name__)
CORS(app)
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Import interfaces
import interfaces.list
import interfaces.recipe
import interfaces.login
import interfaces.meals
import interfaces.profile
