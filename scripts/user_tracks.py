from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from models.track import Track
from models.playlist import Playlist


# Appends tracks to playlist
def append_tracks_to_playlist(playlist, tracks):
    for track in tracks:
        track_info = track['track']

        new_track = Track(
                id=track_info['id'],
                name=track_info['name'],
                artist_name=track_info['artists'][0]['name'],
                popularity=track_info['popularity'],
                duration=track_info['duration_ms'],
                explicit=track_info['explicit'],
            )
        
        playlist.append_track(new_track)


# Returns list os playlists collected via API
def get_user_playlists():
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
        tracks = sp.playlist_items(playlist_id=playlist['id'],
                                fields="items,next", additional_types="tracks")
        new_playlist = Playlist(playlist['id'], playlist['name'])

        append_tracks_to_playlist(new_playlist, tracks['items'])

        while tracks['next']:
            tracks = sp.next(tracks)
            append_tracks_to_playlist(new_playlist, tracks['items'])

        playlists.append(new_playlist)
    
    return playlists