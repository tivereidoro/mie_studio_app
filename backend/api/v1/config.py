#!/usr/bin/env python3
"""Configuration for Flask app
"""


class DevelopmentConfig:
    """Configuration for app in Development stage
    """
    DEBUG = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True


class ProductionConfig:
    """Configuration for app in production stage
    """
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
