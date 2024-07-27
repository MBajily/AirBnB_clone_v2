#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the State with the given <id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states", methods=['GET'], strict_slashes=False)
def states():
    """
    Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template("9-states.html", states=sorted_states)

@app.route("/states/<id>", methods=['GET'], strict_slashes=False)
def states_id(id):
    """
    Displays an HTML page with info about the State with the given <id>, if it exists.
    """
    state = storage.get("State", id)
    if state:
        return render_template("9-states.html", state=state)
    else:
        return render_template("9-states.html")

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