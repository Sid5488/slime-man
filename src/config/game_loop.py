import pygame

from config.users_event import UsersEvent
from config.window import Window


class GameLoop:
    is_looping = True
    window: Window
    users_events: UsersEvent

    def __init__(self):
        self.window = Window()
        self.window.draw()
        self.users_events = UsersEvent()

    def loop(self):
        while self.is_looping:
            self.is_looping = self.users_events.key_events()

            self.update()

    def update(self):
        self.window.draw()

        pygame.display.update()
