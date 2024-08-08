from files import *

tracks = []
artists = []
total_tracks = 0
total_popularity = 0
total_duration = 0
total_explicit = 0
popularity_mean = 0
duration_mean = 0
explict_percentage = 0

def count_stats(track, artist_name=""):
    global total_popularity, total_duration, total_explicit

    if not track.id in tracks:
        total_popularity += track.popularity
        total_duration += track.duration
        total_explicit += track.explicit

        tracks.append(track.id)
        # artists.add(artist_name)

def calculate_analytics():
    global popularity_mean, duration_mean, explict_percentage

    total_tracks = len(tracks)
    popularity_mean = total_popularity / total_tracks
    duration_mean = total_duration / total_tracks
    explict_percentage = total_explicit / total_tracks

    stats = {'total_tracks' : total_tracks,
             'popularity_mean' : popularity_mean,
             'duration_mean' : duration_mean,
             'explicit_percentage' : explict_percentage}
    
    return stats
