from typing import List

import spotipy
from datetime import datetime
from user import get_user_id


def _get_monthly_playlist_name():
    return datetime.utcnow().strftime("%B %Y")


def _get_monthly_playlist_identifier():
    return datetime.utcnow().strftime("%m%y")


def _find_playlist_id_by_name(sp: spotipy.Spotify, playlist_name: str, offset: int = 0):
    playlists_object = sp.current_user_playlists(limit=50, offset=offset)
    playlists = playlists_object['items']

    for playlist in playlists:
        if playlist['name'] == playlist_name:
            return playlist['id']

    # Handle paging
    if playlists_object['next']:
        return _find_playlist_id_by_name(sp, playlist_name, offset + 50)  # 50 is max playlists returned

    return None


def _find_playlist_id_by_description_identifier(sp: spotipy.Spotify, identifier: str, offset: int = 0):
    playlists_object = sp.current_user_playlists(limit=50, offset=offset)
    playlists = playlists_object['items']

    for playlist in playlists:
        if playlist.get('description', "").strip().endswith(identifier):
            return playlist['id']

    # Handle paging
    if playlists_object['next']:
        return _find_playlist_id_by_description_identifier(sp, identifier, offset + 50)  # 50 is max playlists returned

    return None


def _find_playlist_id(sp: spotipy.Spotify, identifier, default_name):
    return (_find_playlist_id_by_description_identifier(sp, identifier) or
            _find_playlist_id_by_name(sp, default_name))


def _create_playlist(sp: spotipy.Spotify, playlist_name: str, description: str):
    return sp.user_playlist_create(get_user_id(sp), playlist_name, description=description)


def _get_monthly_playlist_id(sp: spotipy.Spotify):
    playlist_name = _get_monthly_playlist_name()
    identifier = _get_monthly_playlist_identifier()

    playlist_id = _find_playlist_id(sp, identifier, playlist_name)
    if playlist_id:
        return playlist_id

    return _create_playlist(sp, playlist_name, description=identifier)['id']


def add_songs_to_monthly_playlist(sp: spotipy.Spotify, uris: List[str]):
    if uris:
        sp.playlist_add_items(_get_monthly_playlist_id(sp), items=uris)
