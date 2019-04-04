import pygame, sys


def check_events(hero, game_settings):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                hero.moving_right = True
            if i.key == pygame.K_LEFT:
                hero.moving_left = True
            if i.key == pygame.K_DOWN:
                hero.moving_bottom = True
            if i.key == pygame.K_SPACE:
                hero.make_jump = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                hero.moving_right = False
            if i.key == pygame.K_LEFT:
                hero.moving_left = False
            if i.key == pygame.K_DOWN:
                hero.moving_bottom = False


def update_screen(screen, game_settings, hero):
    if hero.make_jump:
        hero.jump()
    hero.update(screen)
    # hero.blitme()
