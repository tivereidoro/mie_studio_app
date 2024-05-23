#!/usr/bin/env python3
"""More functionality
"""
import bcrypt
from typing import List, Tuple, Dict


def hash_password(password: str) -> str:
    """Hash a password and return it
    """
    if not password or type(password) is not str:
        raise TypeError('password should be str type')
    password = password.encode('utf-8')
    salt_bytes = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt_bytes).decode('utf-8')


def is_list_of_strings(var):
    """Check if variable is a non-empty list of strings
    E.g.
        ['dad'] - True
        ['dad', 'mom'] - True
        [] - False
        other data type - False
    """
    if type(var) is not list or len(var) < 1:
        return False
    return all(isinstance(item, str) for item in var)
