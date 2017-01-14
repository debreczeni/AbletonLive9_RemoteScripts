#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/song_utils.py
from __future__ import absolute_import, print_function

def is_return_track(song, track):
    return track in list(song.return_tracks)


def delete_track_or_return_track(song, track):
    tracks = list(song.tracks)
    if track in tracks:
        track_index = tracks.index(track)
        song.delete_track(track_index)
    else:
        track_index = list(song.return_tracks).index(track)
        song.delete_return_track(track_index)
