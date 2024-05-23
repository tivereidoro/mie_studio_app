#!/usr/bin/env python3
"""App blueprint
"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from backend.api.v1.views.index import *    # noqa: E402
from backend.api.v1.views.user import *    # noqa: E402
from backend.api.v1.views.playlist import *    # noqa: E402
