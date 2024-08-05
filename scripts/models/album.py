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