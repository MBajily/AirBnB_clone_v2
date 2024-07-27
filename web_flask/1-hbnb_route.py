#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


# Route for the homepage
@app.route("/", methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' on the homepage.
    """
    return "Hello HBNB!"


# Route for /hbnb
@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' on the /hbnb route.
    """
    return "HBNB"


if __name__ == "__main__":
    try:
        # Run the Flask app on 0.0.0.0:5000
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        print(f"An error occurred: {e}")
