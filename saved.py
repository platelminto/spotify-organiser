from datetime import datetime, timedelta
import shelve


def get_newly_saved_tracks(sp, offset: int = 0):
    min_tracks_check = 30  # Rarely more than 30 tracks added at a time
    recently_saved_tracks = []

    last_saved_tracks_object = sp.current_user_saved_tracks(limit=min_tracks_check, offset=offset)
    last_saved_tracks = last_saved_tracks_object['items']

    current_checked = datetime.utcnow()  # Store to avoid losing tracks that are added during this process

    with shelve.open('organiser') as db:
        last_checked = db.get('last_checked', default=datetime.utcnow() - timedelta(minutes=600))

    finished = False
    for track_added in last_saved_tracks:
        added_at = datetime.strptime(track_added['added_at'], '%Y-%m-%dT%H:%M:%SZ')
        if added_at > last_checked:
            recently_saved_tracks.append(track_added['track']['uri'])  # Could be uri, URL, or track ID
        # Saved tracks provided in reverse chronological order, so once we're past last check, we can stop.
        else:
            finished = True
            break

    if not finished and last_saved_tracks_object['next']:
        recently_saved_tracks.append(get_newly_saved_tracks(sp, offset + min_tracks_check))

    # Recursive writes will be overwritten by base one.
    with shelve.open('organiser') as db:
        db['last_checked'] = current_checked

    return recently_saved_tracks
