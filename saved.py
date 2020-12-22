from datetime import datetime, timedelta
import shelve


def get_newly_saved_songs(sp, offset: int = 0):
    min_songs_check = 30  # Rarely more than 30 songs added at a time
    recently_saved_songs = []

    last_saved_songs_object = sp.current_user_saved_tracks(limit=min_songs_check, offset=offset)
    last_saved_songs = last_saved_songs_object['items']

    current_checked = datetime.utcnow()  # Store to avoid losing songs that are added during this process

    with shelve.open('organiser') as db:
        last_checked = db.get('last_checked', default=datetime.utcnow() - timedelta(minutes=600))

    finished = False
    for track_added in last_saved_songs:
        added_at = datetime.strptime(track_added['added_at'], '%Y-%m-%dT%H:%M:%SZ')
        if added_at > last_checked:
            recently_saved_songs.append(track_added['track']['uri'])  # Could be uri, URL, or song ID
        # Saved songs provided in reverse chronological order, so once we're past last check, we can stop.
        else:
            finished = True
            break

    if not finished and last_saved_songs_object['next']:
        recently_saved_songs.append(get_newly_saved_songs(sp, offset + min_songs_check))

    # Recursive writes will be overwritten by base one.
    with shelve.open('organiser') as db:
        db['last_checked'] = current_checked

    return reversed(recently_saved_songs)  # Put back into chronological order for playlist order
