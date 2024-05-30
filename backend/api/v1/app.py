#!/usr/bin/env python3
"""API module
"""
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, abort, request, session, make_response
from flask_cors import (CORS, cross_origin)
from backend.api.v1.views import app_views
from backend.api.v1.auth.session_auth import SessionAuth
from pprint import pprint
from werkzeug.exceptions import HTTPException


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
if os.getenv('ENV') == 'production':
    from backend.api.v1.config import ProductionConfig
    configuration = ProductionConfig
else:
    from backend.api.v1.config import DevelopmentConfig
    configuration = DevelopmentConfig

app.config.from_object(configuration)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, supports_credentials=True,
     resources={r"/api/v1/*": {"origins": "*"}})
auth = SessionAuth()


@app.before_request
def do_auth():
    """Perform authentication routines
    """
    # Excluded paths should end with a forward slash '/' except wildcards
    excluded_paths = [
            '/api/v1/stat*',    # status, stats
            '/api/v1/signup/',
            '/api/v1/login/',
            '/api/v1/reset-password/'
        ]
    if not auth.require_auth(request.path, excluded_paths=excluded_paths):
        return

    user = auth.current_user(request)
    if user is None:
        print("No current user or invalid login credentials")
        abort(403)
    else:
        request.current_user = user


@app.errorhandler(Exception)
def not_found(error):
    """
    Generic error handler
    """
    response = {}
    if isinstance(error, HTTPException):
        response['message'] = error.description
        response['status'] = error.code
    else:
        response['message'] = str(error)
        response['status'] = 500

    print(error)
    return make_response(jsonify(response), response['status'])


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized access error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Denied access to a forbidden resource
    Login required
    """
    from backend.api.v1.views import BASE_URI

    return jsonify({
        "error": "Forbidden",
        "next": f"{BASE_URI}/login"}), 403


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
