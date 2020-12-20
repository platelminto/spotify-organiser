import spotipy

from organiser.saved import get_newly_saved_songs
from organiser.playlist import add_songs_to_monthly_playlist

scope = "user-library-read playlist-read-private playlist-read-collaborative " \
        "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope))

add_songs_to_monthly_playlist(sp, get_newly_saved_songs(sp))
