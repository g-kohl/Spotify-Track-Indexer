class Album:
    def __init__(self, id, name, popularity, genres, album_type, total_tracks, release_date):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.genres = genres
        self.album_type = album_type
        self.total_tracks = int(total_tracks)
        self.release_date = release_date

    def __str__(self):
        return self.id + '*' + self.name + '*' + str(self.popularity) + '*' + str(self.genres) + '*' + self.album_type + '*' + str(self.total_tracks) + "*" + self.release_date