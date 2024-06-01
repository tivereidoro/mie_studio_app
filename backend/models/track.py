#!usr/bin/env python3
"""Track module
"""
from backend.models.base import Base


class Track(Base):
    """Track class
    Holds metadata for tracks (songs)
    """
    __tablename__ = 'tracks'
    artist = ''     # Name of artist
    uploader_id = ''
    title = ''
    duration = 0    # In seconds
    extension = ''  # Eg. .ogg, .mp3, .wav
