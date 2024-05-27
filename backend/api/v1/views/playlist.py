#!/usr/bin/env python3
"""Module for playlist views
"""
from backend import models
from flask import jsonify, abort, request, make_response, session
from backend.api.v1.views import app_views, BASE_URI
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
        "uri": f"{BASE_URI}/playlists/{playlist.id}",
        "playlist": playlist.to_json()}), 200


@app_views.route('/playlists/<string:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id) -> str:
    """PUT /playlists
    Parameters:
        - title: string
        - tracks: []    # An array of strings that are track_ids
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
    playlist = Playlist(id=playlist_id, title=data['title'],
                        tracks=data['tracks'])
    playlist.update(session.get('user').get('idToken', ''))
    return jsonify({
        "success": True,
        "message": "Playlist successfully updated",
        "uri": f"{BASE_URI}/playlists/{playlist.id}",
        "playlist": playlist.to_json()}), 200


@app_views.route('/playlists/<string:playlist_id>', methods=['GET'])
def get_playlist_info(playlist_id) -> str:
    """GET /playlists/<playlist_id>
    """
    playlist = models.storage.get(Playlist, playlist_id,
                                  session.get('user').get('idToken', ''))
    if not playlist:
        return jsonify({
            "success": False,
            "message": "Playlist not found"}), 404
    return jsonify({
        "success": True,
        "message": "Playlist info fetched successfully",
        "uri": f"{BASE_URI}/playlists/{playlist.id}",
        "playlist": playlist.to_json()}), 200


@app_views.route('/playlists', methods=['GET'])
def get_all_playlists_info() -> str:
    """GET /playlists
    """
    token = session.get('user').get('idToken', '')
    playlists = firebase.db.child(Playlist.__tablename__).get(token)
    playlists_val = playlists.val()
    for playlist_id, playlist in playlists_val.items():
        playlist['uri'] = f"{BASE_URI}/playlists/{playlist['id']}"
    return jsonify({
        "success": True,
        "message": "All playlists fetched successfully",
        "uri": f"{BASE_URI}/playlists",
        "playlists": playlists_val}), 200


@app_views.route('/playlists', methods=['DELETE'])
def delete_playlist() -> str:
    """DELETE /playlists
    JSON Prameters:
        - playlists: An array of Playlists to delete
    Note: This endpoint is idempotent
    Thus, deleting a non-existing object will return the same result
    as deleting an existing object
    """
    attrs = ['playlists']
    data = request.get_json()
    for attr in attrs:
        if attr not in data:
            return jsonify({
                "success": False,
                "message": f"{attr} is missing"}), 400
    if not is_list_of_strings(data['playlists']):
        return jsonify({
            "success": False,
            "message": "playlists must be a non-empty list of strings"}), 400

    token = session.get('user').get('idToken', '')
    for playlist_id in data['playlists']:
        success = models.storage.delete(Playlist, playlist_id, token)
    playlist = firebase.db.child(Playlist.__tablename__).get(token)
    return jsonify({
        "success": success,
        "message": f"{len(data['playlists'])} Playlist(s) deleted successfully",    # noqa: E501
        "playlists": playlist.val()}), 200
