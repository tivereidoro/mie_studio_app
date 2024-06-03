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
    username = ''

    def to_json(self) -> Dict:
        """Retrieve json value of this object
        """
        result = super().to_json()
        if 'password' in result:
            del result['password']
        return result
