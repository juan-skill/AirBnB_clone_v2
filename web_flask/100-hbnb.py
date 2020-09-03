#!/usr/bin/python3
""" starts a flask web application """


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(self):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb')
def hbnb():
    """ display an Index HTML """
    return render_template('100-hbnb.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(),
                           places=storage.all(Place).values())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
