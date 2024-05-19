#!/usr/bin/python3
""" module to starts a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Closes the storage on teardown"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Displays a list of all State objects present in DBStorage"""
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
