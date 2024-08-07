#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", methods=['GET'], strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBnB filters HTML page.
    """
    st = storage.all("State")
    amen = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=st, amenities=amen)


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
