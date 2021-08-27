#!/usr/bin/env python3
""" [Module that holds basic flask app]
"""

from flask import Flask, render_template
from os import getenv

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Method to setup a basic Flask application
        with a single route and a template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
