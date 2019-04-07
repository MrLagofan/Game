import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, screen, hero):
        super().__init__()

        self.screen = screen
        self.settings = game_settings

        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.x = hero.rect.x + 100
        self.rect.y = hero.usr_y + 100

    def update(self):
        self.rect.x += 6

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
