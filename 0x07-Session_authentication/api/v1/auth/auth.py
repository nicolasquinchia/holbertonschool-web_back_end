#!/usr/bin/env python3
"""[Module that holds auth class]
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """[Class to manage the API authentication]
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[Public method
        that returns True if the path is not
        in the list of strings excluded_paths]

        Args:
            path (str): Path to check
            excluded_paths (List[str]): List of paths excluded

        Returns:
            bool: [False]
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            for index in excluded_paths:
                new_paths = index.find('*')
                if index[:new_paths] == path[:new_paths]\
                        and index.endswith('*'):
                    return False
                else:
                    return True

    def authorization_header(self, request=None) -> str:
        """[Public method, Request validation and
        return the value of the header
        request Authorization]

        Args:
            request ([type]: Defaults to None

        Returns:
            str: [None]
        """
        if request is None:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """[Public method]

        Returns:
            [type]: [None]
        """
        return None

    def session_cookie(self, request=None):
        """[Method that returns a cookie value from a request]
        """
        if request is None:
            return None
        new_cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(new_cookie_name)
