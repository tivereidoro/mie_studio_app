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
from backend.lib.utility import get_track_path
from pprint import pprint


@app_views.route('/tracks', methods=['GET'])
def get_all_tracks_info() -> str:
    """GET /tracks
    """
    token = session.get('user').get('idToken', '')
    tracks = firebase.db.child(Track.__tablename__).get(token).val()
    for track_id in tracks.keys():
        tracks[track_id]['uri'] = f"{BASE_URI}/tracks/{track_id}"
    return jsonify({
        "success": True,
        "message": "All tracks fetched successfully",
        "next": "Follow the uri of any track you want to play",
        "uri": f"{BASE_URI}/tracks",
        "tracks": tracks}), 200


@app_views.route('/tracks/<string:track_id>', methods=['GET'])
def get_download_url(track_id) -> str:
    """GET /tracks/<track_id>
    Note: The 'uri' in the response will allow one to progressively download
    and play the track in the browser
    """
    token = session.get('user').get('idToken', '')
    track = models.storage.get(Track, track_id,
                               session.get('user').get('idToken'))
    if not track:
        return jsonify({
            "success": False,
            "message": "Track not found"}), 404
    path = get_track_path(track)
    uri = firebase.media_store.child(path).get_url(token)
    return jsonify({
        "success": True,
        "message": "Download URL successfully fetched",
        "track": track.to_json(),
        "uri": uri}), 200


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
