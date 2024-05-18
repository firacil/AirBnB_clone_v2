#!/usr/bin/python3
""" module to serve /hbnb webpage"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ serving homepage"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ attribute to serve /hbnb webpage"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """ attribute to serve /c/text webpage"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text):
    """ attribute to serve /python/ or /python/<text>"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    """ attribute to serve /number/<n> webpage"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
