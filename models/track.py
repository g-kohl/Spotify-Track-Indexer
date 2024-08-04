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