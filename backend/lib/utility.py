#!/usr/bin/env python3
"""More functionality
"""
import os
import bcrypt
from typing import List, Tuple, Dict
from backend.models.track import Track


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


def get_track_path(track) -> str:
    """Determine location of track
    """
    if type(track) is not Track:
        raise TypeError('track object is expected')
    path = '/'.join([
        str(os.getenv('AUDIO_DIR')),
        (track.id + track.extension)])
    return path


def create_track_path(track_id, track_extension) -> str:
    """Create track path based on `get_track_path`
    """
    requirements = [track_id, track_extension]
    for obj in requirements:
        if (not obj) or (len(obj) < 1):
            raise TypeError('Non-empty string is expected')
    path = '/'.join([
        str(os.getenv('AUDIO_DIR')),
        (track_id + track_extension)])
    return path
