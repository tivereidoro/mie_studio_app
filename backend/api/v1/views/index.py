#!/usr/bin/env python3
"""Module for index views
"""
from backend.api.v1.views import app_views
from flask import jsonify, abort, request, make_response


@app_views.route('/status', methods=['GET'])
def status() -> str:
    """GET /status
    Return:
        - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/check_session', methods=['GET'])
def check_id():
    """GET /check_session
    Returns current user if session is active
    """
    if not request.current_user:
        abort(401)
    return jsonify(request.current_user), 200
