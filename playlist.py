from typing import List

import spotipy
from datetime import datetime
from user import get_user_id


def _get_monthly_playlist_name():
    return datetime.utcnow().strftime("%B %Y")


def _find_playlist_id(sp: spotipy.Spotify, playlist_name: str, offset: int = 0):
    playlists_object = sp.current_user_playlists(limit=50, offset=offset)
    playlists = playlists_object['items']

    for playlist in playlists:
        if playlist['name'] == playlist_name:
            return playlist['id']

    # Handle paging
    if playlists_object['next']:
        return _find_playlist_id(sp, playlist_name, offset + 50)  # 50 is max playlists returned

    return None


def _create_playlist(sp: spotipy.Spotify, playlist_name: str):
    return sp.user_playlist_create(get_user_id(sp), playlist_name)


def _get_monthly_playlist_id(sp: spotipy.Spotify):
    playlist_name = _get_monthly_playlist_name()

    playlist_id = _find_playlist_id(sp, playlist_name)
    if playlist_id:
        return playlist_id

    return _create_playlist(sp, playlist_name)['id']


def add_songs_to_monthly_playlist(sp: spotipy.Spotify, uris: List[str]):
    if uris:
        sp.playlist_add_items(_get_monthly_playlist_id(sp), items=uris)
