import pygame
from pygame.sprite import Sprite

class Tile(Sprite):
    def __init__(self, x, y, img, group):
        super().__init__()
        self.image = pygame.image.load("img/tile/" + img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        group.add(self)