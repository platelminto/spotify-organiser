import spotipy

from saved import get_newly_saved_songs
from playlist import add_songs_to_monthly_playlist

scope = "user-library-read playlist-read-private playlist-read-collaborative " \
        "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope, open_browser=False))

add_songs_to_monthly_playlist(sp, get_newly_saved_songs(sp))
