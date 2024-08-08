from classification_and_pesquisation import *
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from models.track import Track
from models.playlist import Playlist


def append_tracks_to_playlist(playlist, tracks):
    for track in tracks:
        track_info = track['track']

        new_track = Track(
                id=track_info['id'],
                name=track_info['name'],
                popularity=track_info['popularity'],
                duration=track_info['duration_ms'],
                explicit=track_info['explicit'],
            )
        
        playlist.append_track(new_track)
        count_stats(new_track)


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

stats = calculate_analytics()
print(stats["total_tracks"], stats["popularity_mean"], stats["duration_mean"], stats["explicit_percentage"])

# with open("binaryFileEx.bin", "wb") as file:
#     for p in playlists:
#         for t in p.tracks:
#             write_in_binary_file(t, file)

# file.close()

# with open("binaryFileEx.bin", "rb") as file:
#     for p in playlists:
#         for _ in p.tracks:
#             track_loaded = read_from_binary_file(file)
#             print(track_loaded)

# file.close()
        