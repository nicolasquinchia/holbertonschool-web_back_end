#!/usr/bin/env python3
"""[Basic auth]
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """[Class that inherits from Auth]

    Args:
        Auth ([Class]): [Parent class]
    """

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """ Method Basic - Base64 part,
        Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header[:6] == 'Basic ':
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Method Basic - Base64 decode,
        Returns the decoded value of a Base64
        string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return decode
        except Exception:
            return None
        else:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Method Basic - User credentials,
        Returns the user email and password
        from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        data_spl_list = decoded_base64_authorization_header.split(':', 1)
        return (data_spl_list[0], data_spl_list[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Method Basic - User object,
        Returns the User instance based
        on his email and password
        """
        if not isinstance(user_email, str) or user_email is None:
            return None
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None
        try:
            users_list = User.search({"email": user_email})
        except Exception:
            return None
        for user in users_list:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method Basic - Overload current_user,
        overloads Auth and retrieves the User instance
        for a request
        """
        auth = self.authorization_header(request)
        extract_base64 = self.extract_base64_authorization_header(auth)
        decode_base64 = self.decode_base64_authorization_header(extract_base64)
        extract_user = self.extract_user_credentials(decode_base64)
        user_object = self.user_object_from_credentials(
            extract_user[0], extract_user[1])
        return user_object
