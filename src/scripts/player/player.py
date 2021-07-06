import pygame


class Player:
    slime_man = pygame.sprite.Sprite()

    def __init__(self):
        self.slime_man.image = pygame.image.load(
            'assets/sprite/slime-man/slime-man.png')
        self.slime_man.image = pygame.transform.scale(
            self.slime_man.image, [100, 100])
        self.slime_man.rect = pygame.Rect(50, 50, 100, 100)

    def moving(self, right, left):
        if right != 0 and left == 0:
            self.slime_man.rect.x += right
        elif right == 0 and left != 0:
            self.slime_man.rect.x += -left
