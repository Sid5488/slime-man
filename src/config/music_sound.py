import pygame


class MusicSound:
    music_main: str

    def __init__(self):
        self.music_main = '../../sounds/musics/music_main.wav'

        self.trail_main()

    def trail_main(self):
        pygame.mixer.music.load(self.music_main)
