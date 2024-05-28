#!/usr/bin/env python3
"""Playlist module
"""
from backend.models.base import Base


class Playlist(Base):
    """Playlist class
    Holds track_id's associated to a playlist
    """
    __tablename__ = 'playlists'
    creator_id = ''
    title = ''
    tracks = []
