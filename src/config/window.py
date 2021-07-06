import pygame

from scripts.player.player import Player


class Window:
    WIDTH = 840
    HEIGHT = 480

    display = pygame.display.set_mode([WIDTH, HEIGHT])
    draw_group = pygame.sprite.Group()

    player: Player

    def __init__(self):
        self.player = Player()

    def draw(self):
        pygame.display.set_caption('Meu Super Jogo')
        self.display.fill([46, 46, 46])
        self.group_of_draw()

    def group_of_draw(self):
        self.draw_group.add(self.player.slime_man)
        self.draw_group.draw(self.display)
