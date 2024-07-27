#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/cities_by_states", methods=['GET'], strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with a list of all states and related cities.

    States and cities are sorted by name.
    """
    states = storage.all("State")
    cities_by_state = {}
    for state in states.values():
        cities = [city for city in state.cities]
        cities_by_state[state] = sorted(cities, key=lambda x: x.name)
    
    return render_template("8-cities_by_states.html", cities_by_state=cities_by_state)

@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy session.
    """
    storage.close()

if __name__ == "__main__":
    try:
        # Run the Flask app on 0.0.0.0:5000
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        print(f"An error occurred: {e}")