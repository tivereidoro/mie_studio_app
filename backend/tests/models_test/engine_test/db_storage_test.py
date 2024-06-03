#!/usr/bin/env python3
"""Test for Database Storage
"""
import pytest
from backend.models.engine.db_storage import realtime_DBStorage


@pytest.fixture
def storage_instance():
    return realtime_DBStorage()


def test___init__(storage_instance):
    """Ensure Storage instance is created
    """
    assert isinstance(storage_instance, realtime_DBStorage) is True


def test_all_methods(storage_instance):
    """Ensure storage instance has all required methods
    """
    methods_to_check = ['save', 'update', 'delete', 'get']

    for method in methods_to_check:
        assert hasattr(storage_instance, method) is True
