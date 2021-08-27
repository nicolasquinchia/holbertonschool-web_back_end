#!/usr/bin/env python3
""" [Module that holds Mock logging in]
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from os import getenv

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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


app.config.from_object('4-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Method to setup a basic Flask application
        with a single route and a template
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Method that determines the best
        match to the supported languages
    """
    supported_lang = app.config.get("LANGUAGES")
    supported_arg = request.args.get("locale")
    if supported_arg in supported_arg:
        return supported_arg
    return request.accept_languages.best_match(supported_lang)


def get_user():
    """ Method that returns a user dictionary or None
        if the ID cannot be found or if login_as was not passed
    """
    login_as = request.args.get("login_as")
    if login_as:
        new_user = users[int(login_as)]
        return new_user
    else:
        return None


@app.before_request
def before_request():
    """ Method that finds a user, if any,
        and sets it as global in flask.g.user
    """
    g.user = get_user()


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
