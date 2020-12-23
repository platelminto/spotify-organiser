from typing import List

import spotipy
from datetime import datetime

from playlist import find_playlist_id, create_playlist
from config import MONTHLY_PLAYLIST_FORMAT


def _get_monthly_playlist_name():
    return datetime.utcnow().strftime(MONTHLY_PLAYLIST_FORMAT)  # Spotify Web API uses UTC+0


def _get_monthly_playlist_id(sp: spotipy.Spotify):
    playlist_name = _get_monthly_playlist_name()
    playlist_id = find_playlist_id(sp, playlist_name)

    if playlist_id:
        return playlist_id

    return create_playlist(sp, playlist_name)['id']


def add_tracks_to_monthly_playlist(sp: spotipy.Spotify, uris: List[str]):
    playlist_id = _get_monthly_playlist_id(sp)

    if uris:
        sp.playlist_add_items(playlist_id, items=uris)
