#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
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

# Route for /c/<text>
@app.route("/c/<path:text>", methods=['GET'], strict_slashes=False)
def c(text):
    """
    Displays 'C' followed by the value of <text>.
    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return f"C {text}"

# Route for /python/(<text>)
@app.route("/python", methods=['GET'], defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<path:text>", methods=['GET'], strict_slashes=False)
def python(text):
    """
    Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return f"Python {text}"

# Route for /number/<n>
@app.route("/number/<int:n>", methods=['GET'], strict_slashes=False)
def number(n):
    """
    Displays '<n> is a number' only if n is an integer.
    """
    return f"{n} is a number"

if __name__ == "__main__":
    try:
        # Run the Flask app on 0.0.0.0:5000
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        print(f"An error occurred: {e}")