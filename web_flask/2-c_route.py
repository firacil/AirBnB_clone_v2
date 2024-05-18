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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
