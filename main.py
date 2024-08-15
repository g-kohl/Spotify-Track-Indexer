from classification_and_pesquisation import *
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from models.playlist import Playlist


name_tree = BTree(50)
loaded_tree = BTree(50)
popularity_table = init_popularity_table()

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
                               fields="items,next",
                               additional_types="tracks")
    
    new_playlist = Playlist(playlist['id'], playlist['name'])

    append_tracks_to_playlist(new_playlist, tracks['items'])

    while tracks['next']:
        tracks = sp.next(tracks)
        append_tracks_to_playlist(new_playlist, tracks['items'])

    playlists.append(new_playlist)

stats = calculate_analytics()
# print(stats["total_tracks"], stats["popularity_mean"], stats["duration_mean"], stats["explicit_percentage"])


with open("tracks_file.bin", "ab") as file:
    for p in playlists:
        for t in p.tracks:
            name_tree.insert((t.name, file.tell()))
            popularity_table[t.popularity].append(file.tell())
            write_in_binary_file(t, file)

    file.close()

with open("btree.bin", "wb") as file:
    write_in_binary_file(name_tree, file)

    file.close()

with open("inverted_popurity_file.bin", "wb") as file:
    write_in_binary_file(popularity_table, file)

    file.close()

with open("btree.bin", "rb") as file:
    loaded_tree = read_from_binary_file(file)

    file.close()

track_pointer = loaded_tree.search_key("Overkill")

with open("tracks_file.bin", "rb") as file:
    file.seek(track_pointer)
    track_loaded = read_from_binary_file(file)

    file.close()

print(track_loaded)

with open("inverted_popurity_file.bin", "rb") as file:
    loaded_table = read_from_binary_file(file)

    file.close()

lista100musicas = []

with open("tracks_file.bin", "rb") as file:
    track_counter = 0
    i = 0

    while track_counter < 100:
        for track_pointer in loaded_table[100-i]:
            file.seek(track_pointer)
            loaded_track = read_from_binary_file(file)
            lista100musicas.append(loaded_track)
            track_counter += 1

        i += 1

    file.close()

for track in lista100musicas:
    print(track)

# with open("binaryFileEx.bin", "rb") as file:
#     for p in playlists:
#         for _ in p.tracks:
#             track_loaded = read_from_binary_file(file)
#             print(track_loaded)

# file.close()
