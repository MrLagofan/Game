import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, screen, hero):
        super().__init__()

        self.screen = screen
        self.settings = game_settings

        self.image = pygame.image.load("img/arrow.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.image = pygame.transform.rotate(self.image, 10)
            #pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.x = hero.rect.x + 100
        self.rect.y = hero.rect.y + 100
        self.rotate_arrow = True

    def trans1(self):
        self.rect = pygame.transform.rotate(self.rect, 1)

    def update(self):
        self.rect.x += 6

    def draw_bullet(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
            #draw.rect(self.screen, self.settings.bullet_color, self.rect)
    #if x > self.screen_rect.right:
     #   def __del__(self):
      #      self.draw_bullet()
