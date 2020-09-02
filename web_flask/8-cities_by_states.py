#!/usr/bin/python3
""" starts a flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(self):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states')
def states_list():
    """ /cities_by_states: display all city of a State object """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port='5000')
