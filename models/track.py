import pickle

class Track:
    def __init__(self, id, name, popularity, duration, explicit, external_URLs):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.duration = int(duration)
        self.explicit = explicit
        self.external_URLs = external_URLs

    def write_track_in_binary(self, file):
        pickle.dump(self, file)

    def read_track_from_binary(self, file):
        return pickle.load(self, file)