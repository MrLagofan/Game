import pygame, sys
from bullet import Bullet

def check_events(hero, game_settings, bullets, screen):
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
            if i.key == pygame.K_UP:
                hero.make_jump = True
            if i.key == pygame.K_SPACE:
                new_bullet = Bullet(game_settings, screen, hero)
                bullets.add(new_bullet)
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                hero.moving_right = False
            if i.key == pygame.K_LEFT:
                hero.moving_left = False
            if i.key == pygame.K_DOWN:
                hero.moving_bottom = False


def update_screen(screen, game_settings, hero, bullets):
    if hero.make_jump:
        hero.jump()
    hero.update(screen)
    for bullet in bullets:
        bullet.draw_bullet()
        bullet.update()
    # hero.blitme()
