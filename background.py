import pygame

class Background():
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.g_s = game_settings
        self.bg = pygame.image.load("img/_12_background.png").convert()
        self.bg = pygame.transform.scale(self.bg, (1024, 768))
    def update(self, screen, game_settings):
        if screen.rect.left > image_rect.right:
            screen.width= image.rect.x * 2