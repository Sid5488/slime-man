import pygame


class Window:
    WIDTH = 840
    HEIGHT = 480

    display = pygame.display.set_mode([WIDTH, HEIGHT])
    draw_group = pygame.sprite.Group()

    def draw(self):
        pygame.display.set_caption('Meu Super Jogo')
        self.display.fill([46, 46, 46])
        self.render_elements()

    def render_elements(self, elements=[]):
        for element in elements:
            self.draw_group.add(element)

        self.draw_group.draw(self.display)
