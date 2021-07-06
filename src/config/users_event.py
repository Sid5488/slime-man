import pygame

from scripts.player.player import Player


class UsersEvent:
    exit: bool
    player: Player

    def __init__(self):
        self.player = Player()

    def key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = False
            else:
                self.exit = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.player.moving(1, 0)
        elif keys[pygame.K_a]:
            self.player.moving(0, -1)

        if self.exit:
            return True
        else:
            return False
