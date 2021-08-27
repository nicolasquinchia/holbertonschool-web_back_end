#!/usr/bin/env python3
""" [Module that holds Get locale from request]
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Class that setup the languages ​​available
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
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ Method that determines the best
        match to the supported languages
    """
    supported_lang = app.config.get("LANGUAGES")
    return request.accept_languages.best_match(supported_lang)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
