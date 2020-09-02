#!/usr/bin/python3
""" Starts flask web application Airbnb """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(self):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def states_cities(id=''):
    """ /states and /states/<id> """
    return render_template('9-states.html',
                           states=storage.all(State).values(), id=id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
