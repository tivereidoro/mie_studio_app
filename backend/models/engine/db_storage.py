#!/usr/bin/env python3
"""Connecting to Realtime storage engine
"""
from typing import Any

from backend.api.v1 import firebase
from backend.models.base import Base
from backend.models.user import User
from backend.models.playlist import Playlist
from backend.models.track import Track


classes = {
        "Base": Base, "User": User, "Playlist": Playlist, "Track": Track
        }


class realtime_DBStorage:
    """
    Class for storing data in Firebase Realtime database engine
    Attributes:
        - config_attrs : List
        - firebase: Object # Interacts with Firebase app
        - db: Instance of Realtime database
    """
    def __init__(self):
        """
        Initialize database -> root of the database
        """
        self.db = firebase.db

    def save(self, obj, token):
        """
        Save an object: for new objects existing ones
        Parameters:
            - obj: object to add in database
            - token: user access token
        return: True if successful, else False
        """
        s_table = str(obj.__tablename__)
        try:
            self.db.child(s_table).child(obj.id).set(obj.to_json(), token)
        except Exception as e:
            print("Error in creating new object:", e)
            return False
        return True

    def update(self, obj, token):
        """
        Update an object: for updating existing ones
        Parameters:
            - obj: object to add in database
            - token: user access token
        return: True if successful, else False
        """
        s_table = str(obj.__tablename__)
        try:
            self.db.child(s_table).child(obj.id).update(obj.to_json(), token)
        except Exception as e:
            print("Error in creating new object:", e)
            return False
        return True

    def delete(self, cls, id, token):
        """
        Delete a resource from database
        Parameters:
            - cls: Class of the object to retrieve
            - id: ID of the object to retrieve
            - token: user access token
        return: True if successful else False
        """
        if cls not in classes.values():
            return False

        try:
            self.db.child(cls.__tablename__).child(id).remove(token)
        except Exception as e:
            print("Error in deleting object:", e)
            return False
        return True

    def get(self, cls, id, token):
        """
        Retrieves an object from storage based on its class and ID
        Parameters:
            - cls: Class of the object to retrieve
            - id: ID of the object to retrieve
            - token: user access token
        return: Object instance, or None if not found
        """
        if cls not in classes.values():
            return None

        try:
            if token and type(token) is str  and len(token) > 0:
                matches = self.db.child(cls.__tablename__).child(id).get(token).val()   # noqa: 501
            else:
                matches = self.db.child(cls.__tablename__).child(id).get().val()    # noqa: 501
            if matches:
                if cls is User:
                    # A password retrieved from database was previously hashed
                    # before storage
                    obj = User(hashed=True, **matches)
                else:
                    obj = classes[cls.__name__](**matches)
                return obj
        except Exception as e:
            print("Error getting object from storage:\n", e)
        return None

    def search(self, cls, token, attr: str = '', val: Any = None):
        """
        Retrieve objects with specified attributes
        Parameters:
            - cls: a model class e.g User, Category
            - token: user access token
            - attrs: dict   # a list of attribute and the value
                e.g {'name': 'Histology'}
        Return:
            - [{'path': match}, {'path2': mathc2}]  # A list of matches
        """
        matches = []
        if not attr or not val or not cls or cls not in classes.values():
            raise ValueError('Invalid arguments')
        if len(attr) == 0:
            raise ValueError("attr must be a string of more \
than one characters")
        try:
            all_objects = self.db.child(cls.__tablename__).get(token)
            for obj in all_objects.each():
                obj_val = obj.val()
                if obj_val[attr] == val:
                    matches.append(obj_val)
        except Exception as e:
            print("Exception in finding category: {}".format(e))   # test
            return None
        return matches
