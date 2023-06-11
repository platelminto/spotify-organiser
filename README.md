# spotify-organiser
Organises saved Spotify songs into playlists. Every time it runs, the script checks for any newly saved songs and adds them to certain playlists.

## Installation

Requires Python 3.6 or above. Run the below command from the root directory to install necessary requirements:

    pip install -r requirements.txt


## Usage

Copy `example.env` into `.env` and fill out the appropriate variables`SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` corresponding to their values in your Spotify Application (it's easy & free - make one [here](https://developer.spotify.com/dashboard/applications)). You can leave the default redirect url. Run `main.py` and follow the authentication process (you only have to do this once).

Run periodically. On reach run, the script will add newly saved songs to either:

- Monthly playlists: identified by a {month}{year} identifier at the end of the playlist's description (e.g. '0123' for January 2023). If the playlist doesn't exist, it will create one with a default name, along with a description which includes the identifier. Using monthly playlists means more automatic playlist management: every month, a new playlist will be created, and songs will be added to it until the next month.
- Marked playlists: identified by `MARKED_PLAYLIST_STRING` (as defined in `.env`) at the end of the playlist's description. You must manually add this string to the description of the playlist you want songs to be added to. For example, setting `MARKED_PLAYLIST_STRING=#`, songs will be added to whichever playlist's description ends with a `#`. Using marked playlists means you decide when you want new songs to go to a new playlist - do this by removing `MARKED_PLAYLIST_STRING` from the old playlist description and appending it to the new one.

To use monthly playlists, make sure to still include `MARKED_PLAYLIST_STRING`, but leave it empty.

I'd suggest running it roughly every 20 minutes. Use a VPS (e.g. [Amazon EC2](https://aws.amazon.com/ec2/)) to avoid downtime, or an always-on local machine.

## Features

- Add newly saved songs to a monthly playlist, or one marked by a specific string.

## crontab

If you are using `cron` to schedule the job running, maybe copy this:

```
* * * * *  (cd /home/<user>/dev/spotify-organiser ; venv/bin/python main.py)
```

## To do

- Use last.fm to find the genre of liked songs and add to genre playlists (config file will define which last.fm genres to link to which playlists). Is more problematic than it seems because last.fm doesn't actually provide genre info for a lot of songs, and even artists.
