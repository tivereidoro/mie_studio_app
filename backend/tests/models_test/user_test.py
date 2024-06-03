#!/usr/bin/env python3
"""Test on User
"""
import pytest
from backend.models.user import User


@pytest.fixture
def user_instance():
    return User(email='user@test.com', username='user')


def test_to_json(user_instance):
    """Ensure to_json returns dictionary
    """
    assert type(user_instance.to_json()) is dict
