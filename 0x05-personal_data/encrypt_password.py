#!/usr/bin/env python3
"""This module contains encryption passwords
"""

import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """Function that expects one string argument
    Args:
        password (str)
    Returns:
        bytes: Hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password:  bytes, password: str) -> bool:
    """Function that expects two arguments,
    validate that the provided password matches
    the hashed password
    Args:
        hashed_password (bytes)
        password (str)
    Returns:
        bool: [Boolean]
    """
    new_password = password.encode('utf-8')
    if bcrypt.checkpw(new_password, hashed_password):
        return True
    else:
        return False
