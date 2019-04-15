import pygame, sys

class Robin_hood():


    def __init__(self, screen, game_settings):
        self.screen = screen
        self.g_s = game_settings

        self.image = pygame.image.load("img/Archer.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = 0

        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_up = False

        self.make_jump = False
        self.jump_counter = 30
        self.rect.y = game_settings.height - 360



    def blitme(self, bg):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


    def update(self, screen):
        if self.moving_right:
            self.rect.x  += 3
            #self.g_s.CameraX += 1
        if self.moving_right and self.rect.right > self.screen_rect.right:
            self.rect.x = 0

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= 3
            #self.g_s.CameraX -= 1

        #if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            #self.rect.y += 3
            #self.g_s.CameraX += 6

    def jump(self, game_settings):

        if self.jump_counter >= -30:
            self.rect.y -= self.jump_counter / 3
            self.jump_counter -= 1

        else:
            self.jump_counter = 30
            self.make_jump = False
            self.rect.y = game_settings.height - 360


