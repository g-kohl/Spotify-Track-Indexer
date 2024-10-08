class Playlist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tracks = []

    def __str__(self):
        return self.id + '*' + self.name
    
    def append_track(self, track):
        self.tracks.append(track)

    def length(self):
        return len(self.tracks)
