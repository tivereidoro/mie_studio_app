#!/usr/bin/env python3
"""User module
"""
from backend.lib import utility
from backend.models.base import Base
from typing import Dict


class User(Base):
    """User class
    """
    __tablename__ = 'users'
    email = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, hashed=False, **kwargs):
        super().__init__(*args, **kwargs)
        if not hashed:
            self.password = utility.hash_password(self.password)

    def to_json(self) -> Dict:
        """Retrieve json value of this object
        """
        result = super().to_json()
        if 'password' in result:
            del result['password']
        return result
