# spotify-organiser
Organises saved Spotify songs into monthly and genre playlists.

## Installation

Requires Python 3.6 or above. Run the below command from the root directory to install necessary requirements:

    pip install -r requirements.txt


## Usage

Copy `example.env` into `.env` and fill out the appropriate variables`SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` corresponding to their values in your Spotify Application (make one [here](https://developer.spotify.com/dashboard/applications)). You can leave the default redirect url. Run `main.py` and follow the authentication process (you only have to do this once).

Run again periodically: every time it runs, newly saved songs are added either to a monthly playlist, identified by a {month}{year} identifier at the end of the description, or a playlist description ending with a '#' character. If the playlist doesn't exist, it will create one with a default title. I'd suggest running it roughly every 20 minutes. Use a VPS (e.g. [Amazon EC2](https://aws.amazon.com/ec2/)) to avoid downtime.

## Features

- Add newly saved songs to a monthly playlist, or one with a description ending with a '#' character.

## To do

- Use last.fm to find the genre of liked songs and add to genre playlists (config file will define which last.fm genres to link to which playlists). Is more problematic than it seems because last.fm doesn't actually provide genre info for a lot of songs, and even artists.
