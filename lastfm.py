import os

import requests


def _get(method, payload):
    url = 'http://ws.audioscrobbler.com/2.0/'

    payload['format'] = 'json'
    payload['method'] = method
    payload['api_key'] = os.environ['LASTFM_KEY']
    payload['username'] = os.environ['LASTFM_USERNAME']

    response = requests.get(url, params=payload)
    return response.json()


# Was looking into adding over least listened to tracks from previous month to next one but these are often
# not the most recently added ones, which is what I actually want to move over. Currently unused.
def get_track_playcount(name, artist):
    track_info = _get('track.getInfo', {
        'track': name,
        'artist': artist,
    })

    print(track_info)

    return int(track_info['track']['userplaycount'])


def get_track_genres(name, artist):
    track_info = _get('track.gettoptags', {
        'track': name,
        'artist': artist,
    })

    print(track_info)


def get_album_genres(album, artist):
    album_info = _get('album.gettoptags', {
        'album': album,
        'artist': artist,
    })

    print(album_info)


get_track_genres('Uhhh', 'Louis The Child')
get_album_genres('Candy II', 'Louis The Child')
get_track_genres('Snakes and Birds', 'Deca')
print(get_track_playcount('Uhhh', 'Louis The Child'))