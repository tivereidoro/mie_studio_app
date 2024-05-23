#!/usr/bin/env python3
"""Handle authentication
"""
import os
from flask import request, session
from typing import List, TypeVar
from backend.api.v1 import firebase


class SessionAuth:
    """Session authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Demand authentication for all paths except excluded paths
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if type(path) is str and path[-1] != '/':
            path = path + '/'
        for excluded in excluded_paths:
            if excluded[-1] == '*':
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False
        return True

    def current_user(self, request=None) -> TypeVar('User'):
        """Check the current user
        """
        if request is None:
            return

        try:
            user = session.get('user', None)
            # Refresh token
            user['idToken'] = firebase.auth.refresh(user['refreshToken'])
            session['user'] = user
        except Exception as e:
            print(f"Unkown Server error -> {e}")
            user = None
        return user
