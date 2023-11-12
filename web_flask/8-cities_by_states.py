#!/usr/bin/python3
""" Starts a Flask web app """


from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays list of states and cities from DB """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    cities = sorted(list(storage.all(City).values()), key=lambda x: x.name)
    return render_template(
        '8-cities_by_states.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown(error=None):
    """ Closes current SQLAlchemy Sesh """
    current_storage = getattr(g, "storage", None)
    if current_storage is not None:
        g.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)