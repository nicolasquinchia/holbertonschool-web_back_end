#!/usr/bin/env python3
""" Module that holds,
    New view for Session Authentication
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Method login, that create a new
        view for Session Authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({'email': email})
    except Exception():
        return jsonify({"error": "no user found for this email"}), 404
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for index in user:
        if not index.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            session_user_id = index.id
            new_session_id = auth.create_session(session_user_id)
            json = jsonify(index.to_json())
            session_name = getenv('SESSION_NAME')
            json.set_cookie(session_name, new_session_id)
            return json


@app_views.route('auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ Method logout, that delete a session ID
    """
    from api.v1.app import auth
    destroy = auth.destroy_session(request)
    if destroy is False:
        abort(404)
    return jsonify({}), 200
