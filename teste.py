from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from models import *

load_dotenv()

clientId = os.getenv("SPOTIPY_CLIENT_ID")
clientSecret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirectUri = os.getenv("SPOTIPY_REDIRECT_URI")

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=clientId,
                                               client_secret=clientSecret,
                                               redirect_uri=redirectUri))


results = sp.current_user_playlists()

playlists = []

for _, playlist in enumerate(results['items']):
    items = sp.playlist_items(playlist['uri'])['items']
    new_playlist = Playlist(playlist['id'], playlist['name'])

    for item in items:
        trackObj = item['track']
        try:
            new_playlist.append_track(
                Track(
                    trackId=trackObj['id'],
                    name=trackObj['name'],
                    duration=trackObj['duration_ms'],
                    explicit=trackObj['explicit'],
                    popularity=trackObj['popularity'],
                )
            )
        except:
            print("Track parsing error")
    
    playlists.append(new_playlist)