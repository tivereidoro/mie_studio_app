#!/usr/bin/env python3
"""Test for Utility module
"""
import pytest
from backend.lib import utility
from backend.models.track import Track


@pytest.mark.parametrize('list_input, list_output', [
    (['dad'], True),
    (['dad', 'mom'], True),
    ([], False),
    (['dad', 425], False),
    ([53, 425], False),
    (['d'], True),
    ('dad', False),
    (('dad', 'mom'), False),
    (['dad', ['dsad', 'dada'], 'mom'], False),
    (4252, False),
    ({'dad': 'hello', 'mom': 'world'}, False),
    (425.42424, False)
])
def test_is_list_of_strings(list_input, list_output):
    """Ensure a variable is a non-empty list of strings
    """
    assert utility.is_list_of_strings(list_input) is list_output


def test_get_track_path_correct_value():
    """Ensure determination of track location
    Name of a track is the id + extension
    """
    track = Track(extension='.mp3')
    assert utility.get_track_path(track).split('/')[-1] == (track.id + track.extension)


@pytest.mark.parametrize('arg', [
    ('9024-24-423-5243'),
    (424525),
    (['244', '24']),
    ({'da': 4242, 'mo': '42525-53-53'})
])
def test_get_track_path_wrong_arg(arg):
    """Ensure error is raised
    """
    with pytest.raises(Exception):
        utility.get_track_path(arg)
