import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,screen, game_settings):
        super().__init__()

        self.screen = screen
        self.g_s = game_settings
        self.image = pygame.image.load("img/_WALK_000.png")
        self.image = pygame.transform.scale(self.image, (250, 200))
        self.x = 600
        self.y = game_settings.height - 400
        self.counter = 0
        self.counterbin = 1
        self.lep = True



    def update(self):
        if self.counterbin == 1:
            if self.counter < 200:
                self.x += 2
                self.counter += 1
            elif self.counter == 200:
                self.counterbin = 2
        if self.counterbin == 2:
            if self.counter > 0:
                self.x -= 2
                self.counter -= 1
            elif self.counter == 0:
                self.counterbin = 1



    def draw_enemy(self):
        self.screen.blit(self.image, (self.x, self.y))



