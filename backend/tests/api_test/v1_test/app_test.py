#!/usr/bin/env python3
"""Test App
"""
import pytest
from backend.api.v1.app import app
from backend import status


@pytest.fixture
def client():
    """Yield a client for testing
    """
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_non_existing_endpoint(client):
    """Ensure non-existing endpoint is forbidden for security purposes
    """
    response = client.get('/non-existing-endpoint')
    print(response)
    assert response.status_code == status.FORBIDDEN
