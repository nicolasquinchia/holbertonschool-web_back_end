#!/usr/bin/env python3
""" DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """ DB class
    """

    def __init__(self) -> None:
        """ Method constructor,
            Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Method session,
            Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method create user, which has two required string arguments,
            Returns a User object and save the user to the database
        """
        session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Method Find user, takes in arbitrary keyword arguments,
            Returns the first row found in the users table as
            filtered by the method’s input arguments
        """
        session = self._session
        try:
            find_user = session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError()
        if not find_user:
            raise NoResultFound()
        return find_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Method Update user, takes as argument a required user_id integer
            and arbitrary keyword arguments, Returns None
        """
        updated_user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            user = updated_user.__dict__
            if key in user:
                setattr(updated_user, key, value)
            else:
                raise ValueError
        self._session.commit()
        return None
