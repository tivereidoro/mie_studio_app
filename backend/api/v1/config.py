#!/usr/bin/env python3
"""Configuration for Flask app
"""


class DevelopmentConfig:
    """Configuration for app in Development stage
    """
    DEBUG = True
    SESSION_COOKIE_HTTPONLY = False
    SESSION_COOKIE_SECURE = False


class ProductionConfig:
    """Configuration for app in production stage
    """
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = False
    SESSION_COOKIE_SECURE = False
