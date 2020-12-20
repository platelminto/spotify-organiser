from typing import List

import spotipy
from datetime import datetime


def _get_monthly_playlist_name():
    return datetime.utcnow().strftime("%B %Y")


def _find_playlist(sp: spotipy.Spotify, playlist_name: str, offset: int = 0):
    playlists_object = sp.current_user_playlists(limit=50, offset=offset)
    playlists = playlists_object['items']

    for playlist in playlists:
        if playlist['name'] == playlist_name:
            return playlist['id']

    # Handle paging
    if playlists_object['next']:
        return _find_playlist(sp, playlist_name, offset + 50)  # 50 is max playlists returned

    return None


def get_monthly_playlist(sp: spotipy.Spotify):
    return _find_playlist(sp, _get_monthly_playlist_name())


def add_songs_to_monthly_playlist(sp: spotipy.Spotify, uris: List[str]):
    if uris:
        sp.playlist_add_items(get_monthly_playlist(sp), items=uris)
