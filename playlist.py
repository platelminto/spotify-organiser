from datetime import datetime
from typing import List

import spotipy

from user import get_user_id


class PlaylistTrack:
    def __init__(self, added_at: datetime, uri: str, name: str, artists: List[str]):
        self.added_at = added_at
        self.uri = uri
        self.name = name
        self.artists = artists


def get_playlist_tracks(sp: spotipy.Spotify, playlist_id, offset: int = 0):
    tracks = []
    playlist_object = sp.playlist_items(playlist_id, fields='items(added_at, track(uri,name,artists(name)))',
                                        limit=100, offset=offset)
    for track_info in playlist_object['items']:
        added_at = datetime.strptime(track_info['added_at'], '%Y-%m-%dT%H:%M:%SZ')
        uri = track_info['track']['uri']
        name = track_info['track']['name']
        artists = [artist['name'] for artist in track_info['track']['artists']]

        tracks.append(PlaylistTrack(added_at, uri, name, artists))

    if playlist_object['next']:
        tracks.append(get_playlist_tracks(sp, playlist_id, offset + 100))  # 100 is max tracks returned

    return tracks


def find_playlist_id(sp: spotipy.Spotify, playlist_name: str, offset: int = 0):
    playlists_object = sp.current_user_playlists(limit=50, offset=offset)
    playlists = playlists_object['items']

    for playlist in playlists:
        if playlist['name'] == playlist_name:
            return playlist['id']

    # Handle paging
    if playlists_object['next']:
        return find_playlist_id(sp, playlist_name, offset + 50)  # 50 is max playlists returned

    return None


def create_playlist(sp: spotipy.Spotify, playlist_name: str):
    return sp.user_playlist_create(get_user_id(sp), playlist_name)
