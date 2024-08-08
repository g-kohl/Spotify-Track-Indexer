class Track:
    def __init__(self, id, name, popularity, duration, explicit, artist_name):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.duration = int(duration)
        self.explicit = explicit
        self.artist_name = artist_name

    def __str__(self):
        return self.id + " " + self.name + " " + str(self.popularity) + " " + str(self.duration) + " " + str(self.explicit)