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
            new_track = Track(
                    id=trackObj['id'],
                    name=trackObj['name'],
                    popularity=trackObj['popularity'],
                    duration=trackObj['duration_ms'],
                    explicit=trackObj['explicit'],
                    external_URLs=trackObj['external_urls']
                )
            
            new_playlist.append_track(new_track)
            print(new_playlist.name, new_track.name)
        except:
            print("Track parsing error")
    
    playlists.append(new_playlist)