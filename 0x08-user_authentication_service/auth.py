#!/usr/bin/env python3
""" [Module that holds Auth]
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Method Hash password, it takes in a password
        string argumentsand, Returns bytes
    """
    sal = bcrypt.gensalt()
    password = password.encode()
    return bcrypt.hashpw(password, sal)


def _generate_uuid() -> str:
    """ Method Generate UUIDs, using the uuid module,
        Return a string representation of a new UUID
    """
    new_uuid = str(uuid4())
    return new_uuid


class Auth:
    """ Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method Register user, it takes email and password arguments,
            Return a User object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            register_user = self._db.add_user(email, hashed_password)
            return register_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Method Credentials validation, try to reach the user by email,
            it should expect required arguments by email and password and
            Return a boolean
        """
        try:
            find_user = self._db.find_user_by(email=email)
            password = password.encode()
            valid_login = bcrypt.checkpw(password, find_user.hashed_password)
            return valid_login
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Method Get session ID, it takes an email string argument,
            find the user corresponding to the email, generate a new UUID
            and save it to the database as the user's session_id,
            Return the session ID
        """
        try:
            find_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        self._db.update_user(find_user.id, session_id=_generate_uuid())
        return find_user.session_id

    def get_user_from_session_id(self, session_id: str) -> None:
        """ Method Find user by session ID, it takes a session_id as argument,
            Returns the corresponding User or None
        """
        if session_id is None:
            return None
        try:
            find_user = self._db.find_user_by(session_id=session_id)
            return find_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Method Destroy session, it takes user_id integer argument,
            updates the corresponding user’s session ID to None,
            Returns None
        """
        if user_id is None:
            return None
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Method Generate reset password token, it take an email argument,
            find the user corresponding to the email, Returns a string
        """
        try:
            user_find = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        self._db.update_user(user_find.id, reset_token=_generate_uuid())
        return user_find.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method Update password, it takes reset_token argument and password
            as arguments, use reset_token to find the corresponding user,
            otherwise, hash the password and update the user’s hashed_password
            field with the new hashed password, the reset_token field to None
        """
        try:
            user_find = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_password = _hash_password(password)
        self._db.update_user(
            user_find.id, hashed_password=hashed_password, reset_token=None)
