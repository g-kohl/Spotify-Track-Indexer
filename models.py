class Track:
    def __init__(self, id, name, popularity, duration, explicit, external_URLs):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.duration = int(duration)
        self.explicit = explicit
        self.external_URLs = external_URLs

    def __str__(self):
        return self.id + '*' + self.name + '*' + str(self.popularity) + '*' + str(self.duration) + '*' + str(self.explicit) + '*' + str(self.external_URLs)


class Playlist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # self.followers = int(followers)
        # self.external_URLS = external_URLs
        self.tracks = []

    def __str__(self):
        return self.id + '*' + self.name
    
    def append_track(self, track: Track):
        self.tracks.append(track)

    def length(self):
        return len(self.tracks)


class Artist:
    def __init__(self, id, name, popularity, followers, genres, external_URLs):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.followers = int(followers)
        self.genres = genres
        self.external_URLs = external_URLs

    def __str__(self):
        return self.id + '*' + self.name + '*' + str(self.popularity) + '*' + str(self.followers) + '*' + str(self.genres) + '*' + str(self.external_URLs)


class User:
    def __init__(self, id, name, country, email):
        self.id = id
        self.name = name
        self.country = country
        self.email = email

    def __str__(self):
        return self.id + '*' + self.name + '*' + self.country + '*' + self.email


class Album:
    def __init__(self, id, name, popularity, genres, albumType, totalTracks, releaseDate, external_URLs):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.genres = genres
        self.albumType = albumType
        self.totalTracks = int(totalTracks)
        self.releaseDate = releaseDate
        self.external_URLs = external_URLs

    def __str__(self):
        return self.id + '*' + self.name + '*' + str(self.popularity) + '*' + str(self.genres) + '*' + self.albumType + '*' + str(self.totalTracks) + "*" + self.releaseDate + "*" + self.external_URLs