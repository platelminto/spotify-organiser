import spotipy

from saved import get_newly_saved_songs
from playlist import add_songs_to_monthly_playlist, add_songs_to_hash_playlist

scope = "user-library-read playlist-read-private playlist-read-collaborative " \
        "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope, open_browser=False))

newly_saved_songs = get_newly_saved_songs(sp)
newly_saved_songs.reverse()  # Put back into chronological order for playlist order

add_songs_to_hash_playlist(sp, newly_saved_songs)
