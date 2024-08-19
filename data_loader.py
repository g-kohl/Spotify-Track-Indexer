from classification_and_pesquisation import *

def build_data_structures():
    name_tree = BTree(50)
    prefix_tree = PrefixTree()
    popularity_table = init_popularity_table()

    # builds name tree and popularity table using tracks from db
    with (open("tracks_file.bin", "rb")) as track_db:
        track_ptr = 0
        while True:
            try:
                track = read_from_binary_file(track_db)

                name_tree.insert((track.name, track_ptr))
                popularity_table[track.popularity].append(track_ptr)
                prefix_tree.insert(track.name.lower(), track_ptr)

                track_ptr = track_db.tell()
            except EOFError:
                break
        track_db.close()

    # writes name tree and popularity in files
    with open("btree.bin", "wb") as file:
        write_in_binary_file(name_tree, file)

        file.close()

    with open("inverted_popurity_file.bin", "wb") as file:
        write_in_binary_file(popularity_table, file)

        file.close()

    with open("trie.bin", "wb") as file:
        write_in_binary_file(prefix_tree, file)

        file.close()

def generate_analytics():
    total_popularity = 0
    total_duration = 0
    total_explicit = 0
    tracks = []

    with open("tracks_file.bin", "rb") as track_db:
        while True:
            try:
                track = read_from_binary_file(track_db)

                if not track.id in tracks:
                    total_popularity += track.popularity
                    total_duration += track.duration
                    total_explicit += track.explicit
                    tracks.append(track.id)

            except EOFError:
                break
        track_db.close()

    total_tracks = len(tracks)
    popularity_average = total_popularity / total_tracks
    duration_average = total_duration / total_tracks
    explict_percentage = total_explicit / total_tracks

    calculated_stats = {'total_tracks' : total_tracks,
                        'popularity_average' : popularity_average,
                        'duration_average' : duration_average,
                        'explicit_percentage' : explict_percentage}
    
    return calculated_stats

def load_name_tree():
    with open("btree.bin", "rb") as file:
        loaded_tree = read_from_binary_file(file)

        file.close()

    return loaded_tree


def load_popularity_table():
    with open("inverted_popurity_file.bin", "rb") as file:
        loaded_table = read_from_binary_file(file)

        file.close()

    return loaded_table


def load_prefix_tree():
    with open("trie.bin", "rb") as file:
        loaded_tree = read_from_binary_file(file)

        file.close()

    return loaded_tree


# given a track pointer, searches it in track_db
def get_track(track_pointer, track_db):
    track_db.seek(track_pointer)
    track_loaded = read_from_binary_file(track_db)

    return track_loaded


def get_tracks_order_by_popularity(num, is_descending, popularity_table):
    top_tracks = list()

    with open("tracks_file.bin", "rb") as file:
        track_counter = 0
        popularity = 100 if is_descending else 0
        delta = -1 if is_descending else 1

        while track_counter < num:
            for track_pointer in popularity_table[popularity]:
                try:
                    loaded_track = get_track(track_pointer, file)
                except EOFError:
                    break

                top_tracks.append(loaded_track)

                track_counter += 1

                if track_counter >= num:
                    break

            popularity += delta

        file.close()

    return top_tracks