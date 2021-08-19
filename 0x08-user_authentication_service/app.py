#!/usr/bin/env python3
""" [Module that holds Basic Flask app]
"""

from flask import Flask, jsonify, abort, request, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def basic_flask_app() -> str:
    """ Method Basic Flask app, that create and set up
        a basic Flask app, Return a JSON payload.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Method Register user, Define a users function that implements
        the POST /users route, Return a 400 status code
    """
    email_data = request.form.get('email')
    password_data = request.form.get('password')
    try:
        AUTH.register_user(email_data, password_data)
        return jsonify({"email": email_data, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Method log in, responds to the POST / sessions path,
        create a new session for the user, save the session id as a cookie,
        Return a JSON payload of the form
    """
    email_data = request.form.get("email")
    password_data = request.form.get("password")
    if not AUTH.valid_login(email_data, password_data):
        abort(401)
    else:
        session_id = AUTH.create_session(email_data)
        response = jsonify({"email": email_data, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ Method Log out, responds to the DELETE /sessions route,
        find for the user with the requested session ID
    """
    session_id = request.cookies.get("session_id")
    search_user = AUTH.get_user_from_session_id(session_id)
    if search_user:
        AUTH.destroy_session(search_user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ Method User profile, responds to the GET /profile route,
        the request contains a cookie session_id, to find the user
    """
    session_id = request.cookies.get("session_id")
    search_user = AUTH.get_user_from_session_id(session_id)
    if search_user:
        return jsonify({"email": search_user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ Method Get reset password token, responds to the
        POST /reset_password route, request with form data with
        email field
    """
    email_data = request.form.get('email')
    try:
        new_token = AUTH.get_reset_password_token(email_data)
        return jsonify({"email": email_data, "reset_token": new_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ Method Update password end-point, respond to the PUT /
        reset_password path, request with the data of email,
        reset_token and new_password, Update the password
    """
    new_email = request.form.get("email")
    new_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(new_token, new_password)
        return jsonify({"email": new_email,
                        "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
