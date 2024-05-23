#!/usr/bin/env python3
"""Module for playlist views
"""
from backend import models
from flask import jsonify, abort, request, make_response, session
from backend.api.v1.views import app_views
from backend.models.playlist import Playlist
from backend.api.v1 import firebase
from backend.lib.utility import is_list_of_strings
from pprint import pprint


@app_views.route('/playlists', methods=['POST'])
def create_new_playlist() -> str:
    """POST /playlists
    Parameters:
        - title: string
        - tracks: []    # An array of strings that are track_ids
    Note: a Playlist will not be created if there are no track_ids to add
    """
    attrs = ['title', 'tracks']
    data = request.get_json()
    for attr in attrs:
        if attr not in data:
            return jsonify({
                "success": False,
                "message": f"{attr} is missing"}), 400
    if not is_list_of_strings(data['tracks']):
        return jsonify({
            "success": False,
            "message": "tracks must be a non-empty list of strings"}), 400
    playlist = Playlist(title=data['title'], tracks=data['tracks'],
                        creator_id=session.get('user').get('localId', ''))
    playlist.save(session.get('user').get('idToken', ''))
    return jsonify({
        "success": True,
        "message": "Playlist created successfully",
        "playlist": playlist.to_json()}), 200
