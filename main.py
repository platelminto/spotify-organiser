import spotipy

from saved import get_newly_saved_tracks
from monthly import add_tracks_to_monthly_playlist

scope = "user-library-read playlist-read-private playlist-read-collaborative " \
        "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope, open_browser=False))

newly_saved_tracks = get_newly_saved_tracks(sp)
newly_saved_tracks.reverse()  # Put back into chronological order for playlist order

add_tracks_to_monthly_playlist(sp, newly_saved_tracks)
