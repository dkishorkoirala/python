class MusicPlayer:
    def play(self):
        print("Playing music...")


class MP3Player(MusicPlayer):
    def play(self):
        print("Playing MP3 player music...")


class StreamingPlayer(MusicPlayer):
    def play(self):
        super().play()
        print("Playing Streaming music...")


for music in [MusicPlayer(), MP3Player(), StreamingPlayer()]:
    music.play()
