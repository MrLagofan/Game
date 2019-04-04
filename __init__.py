import pygame, sys, os
from settings import Settings
from robin_hood import Robin_hood
import game_functions as g_f

clock = pygame.time.Clock()


def init_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    hero = Robin_hood(screen, game_settings)
    pygame.display.set_caption("The best game in the world")
    bg = pygame.image.load("img/_12_background.png").convert()
    bg = pygame.transform.scale(bg, (1024, 768))

    x = 0
    while True:
        g_f.check_events(hero, game_settings)
        g_f.update_screen(screen, game_settings, hero)
        #screen.blit(bg, (0 - game_settings.CameraX, 0 - game_settings.CameraY))
        screen.blit(hero.image, (hero.rect.x + game_settings.CameraX, hero.usr_y + game_settings.CameraY))
        pygame.display.flip()
        rel_x = x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < game_settings.width:
            screen.blit(bg, (rel_x, 0))
        x = 9 - hero.rect.x
        clock.tick(60)

init_game()