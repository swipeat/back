#
# Swipeat project main file.
#

# Imports all interfaces
from interfaces import app

# Launch the REST server
if __name__ == "__main__":
    """ Launch the REST server """
    app.run(host='0.0.0.0', port=8080)