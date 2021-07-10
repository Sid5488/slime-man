import pygame

from config.player_events import UsersEvent
from config.window import Window


class GameLoop:
    is_looping = True
    window: Window
    player_events: UsersEvent

    def __init__(self):
        self.window = Window()
        self.window.draw()
        self.player_events = UsersEvent()

    def loop(self):
        while self.is_looping:
            self.is_looping = self.player_events.key_events()

            self.update()

    def update(self):
        self.window.draw()

        pygame.display.update()
