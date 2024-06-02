#!/usr/bin/env python3
"""Test on Track
"""
import pytest
from backend.models.track import Track


@pytest.fixture
def track_instance():
    return Track()


def test_to_json(track_instance):
    """Ensure to_json returns dictionary
    """
    assert type(track_instance.to_json()) is dict
