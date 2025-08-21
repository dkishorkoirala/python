class Playlist:
    def __init__(self, song_names):
        self.song_names = song_names

    def __len__(self):
        return len(self.song_names)


songs = ["song1", "song2", "song3"]
playlist = Playlist(songs)
print(len(playlist))
