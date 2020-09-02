#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def index():
    """ default route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ hbnb path """
    return "HBNB"


@app.route('/c/<text>')
def display_C(text):
    """ return /c/<text> """
    return "C {:s}".format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    """ return /python/<text>"""
    return "Python {:s}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ display n is a number only if n is an integer """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
