#!/usr/bin/env python3
"""Base module for objects
"""
import json
from backend import models
from uuid import uuid4
from datetime import datetime

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'


class Base():
    """Base class
    """
    def __init__(self, *args: list, **kwargs: dict):
        """Initialize a Base instance
        """
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        s_class = str(self.__class__.__name__)
        self.id = kwargs.get('id', str(uuid4()))
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if type(value) is datetime:
                value = value.strftime(TIMESTAMP_FORMAT)
            setattr(self, key, value)

    def to_json(self) -> dict:
        """Convert the object to a JSON dictionary
        Converts all instance attributes to a dictionary and returns it
        """
        result = {}
        result['__class__'] = str(self.__class__.__name__)
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                value = value.strftime(TIMESTAMP_FORMAT)
            result[key] = value
        return result

    def __str__(self):
        """String representation of the Base class"""
        obj_data = self.__dict__.copy()
        return f"[{self.__class__.__name__}] ({self.id}) {obj_data}"

    def save(self, token):
        """Saving changes in the instance
        Parameters:
            - token: user access token
        """
        self.updated_at = datetime.utcnow()
        return models.storage.save(self, token)

    def delete(self, token):
        """Delete the current instance
        Parameters:
            - token: user access token
        """
        return models.storage.delete(self, token)
