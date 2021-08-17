#!/usr/bin/env python3
""" Module that Create a session
"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ Class SessionAuth that inherits from Auth

    Args:
        Auth ([Class]): [Parent class]
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Method that creates a Session
            ID for a user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        new_session_id = str(uuid4())
        self.user_id_by_session_id[new_session_id] = user_id
        return new_session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Method User ID for Session ID,
            Returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        new_user_id = self.user_id_by_session_id.get(session_id)
        return new_user_id

    def current_user(self, request=None):
        """ Method Use Session ID for identifying a User,
            Returns a User instance based on a cookie value
        """
        session = self.session_cookie(request)
        user = self.user_id_for_session_id(session)
        return User.get(user)

    def destroy_session(self, request=None):
        """ Method that deletes the user session / logout
        """
        if request is None:
            return False
        id_session_name = self.session_cookie(request)
        if id_session_name is None:
            return False
        id_user_session = self.user_id_for_session_id(id_session_name)
        if id_user_session is None:
            return False
        del self.user_id_by_session_id[id_session_name]
        return True
