#!/usr/bin/env python3
"""Module for Track views
"""
import os
from backend import models
from flask import jsonify, abort, request, make_response, session
from backend.api.v1.views import app_views, BASE_URI
from backend.models.track import Track
from backend.api.v1 import firebase
from pprint import pprint


@app_views.route('/tracks', methods=['POST'])
def upload_track() -> str:
    """POST /tracks
    Form-data parameters: # Ensure it is a form-data parameter
        - title: string [optional]
        - duration: integer # Duration in seconds
        - payload: file # Must be an audio file

    Note: If title is not passed, the filename becomes the title
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

    if not request.form.get('title'):
        data['title'] = data['payload'].filename
    else:
        data['title'] = request.form.get('title')

    data['extension'] = '.' + data['payload'].filename.split('.')[-1]
    track = Track(uploader_id=session.get('user').get('localId', ''),
                  title=data['title'],
                  duration=data['duration'],
                  extension=data['extension'])

    path = '/'.join([str(os.getenv('AUDIO_DIR')), (track.id + data['extension'])])  # noqa: E501
    token = session.get('user').get('idToken', '')
    firebase.media_store.child(path).put(data['payload'], token)
    # Save track meta data
    track.save(session.get('user').get('idToken', ''))
    return jsonify({
        "success": True,
        "message": "Track successfully uploaded",
        "uri": f"{BASE_URI}/tracks/{track.id}",
        "track": track.to_json()}), 200
