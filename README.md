# spotify-organiser
Organises saved Spotify songs into monthly and genre playlists.

## Installation

Requires Python 3.6 or above. Run the below command from the root directory to install necessary requirements:

    pip install -r requirements.txt


## Usage

Add environment variables `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` corresponding to their values in your Spotify Application (make one [here](https://developer.spotify.com/dashboard/applications)). You can leave the default redirect url. Run `organiser/main.py` and follow the authentication process (you only have to do this once). Run again periodically: every time it runs, newly saved songs are added to a monthly playlist (for example, `December 2020`). I'd suggest using `cron` or similar, roughly every 20 minutes; using a cloud service is optimal to avoid downtime.

## Features

- Add newly saved songs to a monthly playlist.

## To do

- At the beginning of the month, add songs from the end of the previous monthly playlist to the new one (~5 days?).
- Use last.fm to find the genre of liked songs and add to genre playlists (config file will define which last.fm genres to link to which playlists).
