class Track:
    def __init__(self, id, artist_name, name, popularity, duration, explicit):
        self.id = id
        self.artist_name = artist_name
        self.name = name
        self.popularity = int(popularity)
        self.duration = int(duration)
        self.explicit = explicit

    def __str__(self):
        return self.id + " " + self.artist_name + " " + self.name + " " + str(self.popularity) + " " + str(self.duration) + " " + str(self.explicit)