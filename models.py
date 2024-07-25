class Track:
    def __init__(self, trackId, name, popularity, duration, explicit):
        self.trackId = trackId
        self.name = name
        self.popularity = popularity
        self.duration = duration
        self.explicit = explicit


class Playlist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tracks = []
    
    def append_track(self, track: Track):
        self.tracks.append(track)

    def length(self):
        return len(self.tracks)


class Artist:
    def __init__(self, id, name, popularity, followers, genres, external_URLs):
        self.id, self.name, self.popularity, self.followers, self.genres, self.external_URLs = id, name, popularity, followers, genres, external_URLs

    def __str__(self):
        return self.id + self.name + str(self.popularity) + str(self.followers) + str(self.genres) + str(self.external_URLs)


