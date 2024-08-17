from classification_and_pesquisation import *
from scripts.user_tracks import get_user_playlists

# stats = calculate_analytics()
# print(stats["total_tracks"], stats["popularity_mean"], stats["duration_mean"], stats["explicit_percentage"])

# stats should be calculated here
# the ideal scenario is to write the binary file while the tracks are being fetched
# (inside the get_user_playlist function)

playlists = get_user_playlists()

with open("tracks_file.bin", "ab") as file:
    for p in playlists:
        for t in p.tracks:
            write_in_binary_file(t, file)

    file.close()
