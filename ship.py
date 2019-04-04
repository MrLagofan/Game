import pygame

class Ship():


    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("img/Archer.png")
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        self.screen.blit(self.image, self.rect)
