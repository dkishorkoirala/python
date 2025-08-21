class Playlist:
    def __init__(self, song):
        self.song = song

    def __contains__(self, song):
        return song in self.song

    def __add__(self, other):
        if isinstance(other, Playlist):
            return Playlist(self.song + other.song)
        return NotImplemented

    def __mul__(self, times):
        if isinstance(times, int):
            return Playlist(self.song * times)
        return NotImplemented

    def __str__(self):
        return f"Playlist({self.song})"


playlist1 = Playlist(["song1", "song2"])
playlist2 = Playlist(["song3", "song4"])
print("song1" in playlist1)

playlist3 = playlist1 + playlist2
print(playlist3)

playlist4 = playlist3 * 2
print(playlist4)
