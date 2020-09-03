#!/usr/bin/python3
""" Starts Flask web application """


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(self):
    """ remove the SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """ server to the static content """
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
