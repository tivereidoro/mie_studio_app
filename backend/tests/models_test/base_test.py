#!/usr/bin/env python3
"""Test on Base
"""
import pytest
from backend.models.base import Base


@pytest.fixture
def base_instance():
    return Base()


def test___init__(base_instance):
    """Ensure object is returned
    """
    assert isinstance(base_instance, Base) is True


def test_to_json(base_instance):
    """Ensure to_json returns dictionary
    """
    assert type(base_instance.to_json()) is dict


def test___str__(base_instance):
    """Ensure __str__ returns string
    """
    assert type(str(base_instance)) is str
