import spotipy


def get_user_id(sp: spotipy.Spotify):
    return sp.current_user()["id"]
