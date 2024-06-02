#!/usr/bin/env python3
"""Test for Playlist
"""
import pytest
from backend.models.playlist import Playlist

@pytest.fixture
def playlist_instance():
    return Playlist()

def test_to_json(playlist_instance):
    """Ensure to_json returns dictionary
    """
    assert type(playlist_instance.to_json()) is dict
