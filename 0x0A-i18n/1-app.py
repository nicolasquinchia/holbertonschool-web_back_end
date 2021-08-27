#!/usr/bin/env python3
""" [Module that holds basic babel setup]
"""

from flask import Flask, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class that setup the languages ​​available
        in the application, and sets the default Babel
        locale ("en") and time zone ("UTC")
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Method to setup a basic Flask application
        with a single route and a template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
