#!/usr/bin/env python3
"""Module for user views
"""
from backend import models
from flask import jsonify, abort, request, make_response, session
from backend.api.v1.views import app_views
from backend.models.user import User
from backend.api.v1 import firebase
from pprint import pprint


@app_views.route('/signup', methods=['POST'])
def create_user() -> str:
    """POST /signup
    JSON body requirements:
        - username: str
        - email: str
        - password: str
    """
    attrs = ['username', 'email', 'password']
    data = request.get_json()
    for attr in attrs:
        if attr not in data:
            return jsonify({
                "success": False,
                "message": f"{attr} is missing"}), 400
    # Create user
    email = data['email']
    password = data['password']
    username = data['username']
    user = firebase.auth.create_user_with_email_and_password(email, password)
    if not user:
        return jsonify({
            "successs": False,
            "message": "Could not create new user"}), 500
    # Send email verification ASAP
    firebase.auth.send_email_verification(user['idToken'])
    # Continue sign up
    user_obj = User(id=user['localId'], username=username,
                    email=email, password=password)
    if not user_obj.save(user['idToken']):
        return jsonify({
            "success": False,
            "message": "Could not store user to database"}), 500
    return jsonify({"success": True, "user": user_obj.to_json()})


@app_views.route('/login', methods=['POST'])
def login_user() -> str:
    """POSST /login
    JSON body requirements:
        - email: str
        - password: str
    """
    attrs = ['email', 'password']
    data = request.get_json()
    for attr in attrs:
        if attr not in data:
            return jsonify({
                "success": False,
                "message": f"{attr} is missing"}), 400
    # Login user
    email = data['email']
    password = data['password']
    try:
        user = firebase.auth.sign_in_with_email_and_password(email, password)
        user_obj = models.storage.get(User, user['localId'], user['idToken'])
    except Exception as e:
        print("Error in signing in user:", e)
        return jsonify({
            "success": False,
            "message": "Could not log in user. Check login credentials"}), 401
    session['user'] = user
    return jsonify({
        "success": True,
        "message": "Login successful",
        "user": user_obj.to_json()
            }), 200

@app_views.route('/login', methods=['GET'])
def get_session_information() -> str:
    """GET /login
    """
    user = session.get('user')
    try:
        user_obj = models.storage.get(User, user['localId'], user['idToken'])
    except Exception as e:
        print("Error in signing in user:", e)
        return jsonify({
            "success": False,
            "message": "Could not log in user. Check login credentials"}), 401

    return jsonify({"success": True, "user": user_obj.to_json()}), 200
