#
# list.py : Interfaces to access list.
#

from interfaces import app
import json

# /list/get : Get the current list
@app.route("/list/get")
def getList():
    """ Interface /list/get
        Get current lists """
    return json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)