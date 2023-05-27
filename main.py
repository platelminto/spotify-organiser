import os

import spotipy
from dotenv import load_dotenv

from saved import get_newly_saved_songs
from playlist import add_songs_to_monthly_playlist, add_songs_to_marked_playlist

load_dotenv()


scope = (
    "user-library-read playlist-read-private playlist-read-collaborative "
    "playlist-modify-public playlist-modify-private"
)

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")


sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        open_browser=False,
    )
)

newly_saved_songs = get_newly_saved_songs(sp)
newly_saved_songs.reverse()  # Put back into chronological order for playlist order

marked_playlist_string = os.getenv("MARKED_PLAYLIST_STRING", "#")
# If it's not set, we use marked playlists since that was the default pre-.env variable
if marked_playlist_string or "MARKED_PLAYLIST_STRING" not in os.environ:
    add_songs_to_marked_playlist(sp, newly_saved_songs, marked_playlist_string)
else:
    add_songs_to_monthly_playlist(sp, newly_saved_songs)
