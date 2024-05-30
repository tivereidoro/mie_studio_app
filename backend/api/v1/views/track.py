#!/usr/bin/env python3
"""Module for Track views
"""
import os
from mutagen import File as MutagenFile
from backend import models
from flask import jsonify, abort, request, make_response, session
from backend.api.v1.views import app_views, BASE_URI
from backend.models.track import Track
from backend.api.v1 import firebase
from backend.lib.utility import get_track_path, is_list_of_strings
from pprint import pprint


@app_views.route('/tracks', methods=['DELETE'])
def delete_tracks() -> str:
    """DELETE /tracks
    JSON parameter:
        - tracks: An array of track ids
    Note: This URL is idempotent
    """
    attrs = ['tracks']
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

    token = session.get('user').get('idToken', '')
    for track_id in data['tracks']:
        if len(track_id):
            track = models.storage.get(Track, track_id, token)
            if track:
                models.storage.delete(Track, track_id, token)
                firebase.media_store.delete(get_track_path(track), token)
    tracks = firebase.db.child(Track.__tablename__).get(token)
    return jsonify({
        "success": True,
        "message": f"{len(data['tracks'])} Track(s) deleted successfully",
        "tracks": tracks.val()}), 200


@app_views.route('/tracks', methods=['GET'])
def get_all_tracks_info() -> str:
    """GET /tracks
    """
    # token = session.get('user').get('idToken', '')
    # tracks = firebase.db.child(Track.__tablename__).get(token).val()
    tracks = firebase.db.child(Track.__tablename__).get().val()
    for track_id in tracks.keys():
        tracks[track_id]['uri'] = f"{BASE_URI}/tracks/{track_id}"
    return jsonify({
        "success": True,
        "message": "All tracks fetched successfully",
        "next": "Follow the uri of any track you want to play",
        "uri": f"{BASE_URI}/tracks",
        "tracks": tracks}), 200


@app_views.route('/tracks/specified', methods=['GET'])
def get_specified_tracks_only() -> str:
    """
    JSON parameter:
        - tracks: [] An array of tracks ID to get information on
    NB: The download URL of the tracks are not returned, just information
    on the track
    """
    attrs = ['tracks']
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

    # token = session.get('user').get('idToken', '')
    token = ''
    tracks = {}
    for track_id in data['tracks']:
        if len(track_id):
            data = models.storage.get(Track, track_id, token)
            if data:
                tracks[track_id] = data.to_json()
                tracks[track_id]['uri'] = f"{BASE_URI}/tracks/{track_id}"

    return jsonify({
        "success": True,
        "message": "All specified tracks fetched successfully",
        "next": "Follow the uri of any track you want to play",
        "uri": f"{BASE_URI}/tracks/specified",
        "tracks": tracks}), 200


@app_views.route('/tracks/<string:track_id>', methods=['GET'])
def get_playback_uri(track_id) -> str:
    """GET /tracks/<track_id>
    Note: The 'playback_uri' in the response will allow one to \
            progressively download
    and play the track in the browser
    """
    # token = session.get('user').get('idToken', '')
    token = ''
    track = models.storage.get(Track, track_id, token)
    if not track:
        return jsonify({
            "success": False,
            "message": "Track not found"}), 404
    path = get_track_path(track)
    # uri = firebase.media_store.child(path).get_url(token)
    uri = firebase.media_store.child(path).get_url(token)
    track_json = track.to_json()
    track_json['playback_uri'] = uri
    return jsonify({
        "success": True,
        "message": "Playback URI successfully fetched",
        "track": track_json,
        "uri": f"{BASE_URI}/tracks/{track_id}"}), 200


@app_views.route('/tracks', methods=['POST'])
def upload_track() -> str:
    """POST /tracks
    Form-data parameters: # Ensure it is a form-data parameter
        - title: string [optional]
        - duration: integer # Duration in seconds
        - payload: file # Must be an audio file
    Note:
        * If title is not passed, the filename becomes the title
        * If duration can be derived from metadata, this duration attribute
            will be forsaken
    """
    attrs = ['duration', 'payload']
    data = {}
    for attr in attrs:
        if attr == 'payload':
            data[attr] = request.files[attr]
        else:
            data[attr] = request.form.get(attr)
        if not data[attr]:
            return jsonify({"Error": f"Missing parameter -> {attr}"}), 400

    # automatic title
    if not request.form.get('title'):
        data['title'] = data['payload'].filename
    else:
        data['title'] = request.form.get('title')
    # automatic duration
    audio = MutagenFile(data['payload'].stream)
    if audio and hasattr(audio, 'info'):
        data['duration'] = audio.info.length

    # Determine path
    data['extension'] = '.' + data['payload'].filename.split('.')[-1]
    track = Track(uploader_id=session.get('user').get('localId', ''),
                  title=data['title'],
                  duration=data['duration'],
                  extension=data['extension'])

    path = get_track_path(track)

    token = session.get('user').get('idToken', '')
    firebase.media_store.child(path).put(data['payload'], token)
    # Save track meta data
    track.save(session.get('user').get('idToken', ''))
    return jsonify({
        "success": True,
        "message": "Track successfully uploaded",
        "uri": f"{BASE_URI}/tracks/{track.id}",
        "track": track.to_json()}), 200
