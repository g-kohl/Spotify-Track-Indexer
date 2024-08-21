from classification_and_pesquisation import *
from scripts.user_tracks import get_user_playlists


# Saves all loaded tracks in binary file
def database_setup():
    playlists = get_user_playlists()

    with open("tracks_file.bin", "ab") as file:
        for p in playlists:
            for t in p.tracks:
                write_in_binary_file(t, file)

        file.close()
