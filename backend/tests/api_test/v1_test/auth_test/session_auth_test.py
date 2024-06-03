#!/usr/bin/env python3
"""Test for Session Authentication
"""
import pytest
from backend.api.v1.auth.session_auth import SessionAuth
from backend.api.v1.app import excluded_paths


@pytest.fixture
def session_auth():
    """Instance of sesison auth
    """
    return SessionAuth()


@pytest.mark.parametrize('path, result', [
    ('/api/v1/status', False),
    ('/api/v1/stats', False),
    ('/api/v1/stat-foo-bar', False)
])
def test_require_auth(path, result, session_auth):
    """Ensure convention of excluding paths
    """
    assert session_auth.require_auth(path, excluded_paths) is result
