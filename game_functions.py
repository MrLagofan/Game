import pygame, sys
from bullet import Bullet
from enemy import Enemy


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
            if len(bullets) != 5:
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


def update_screen(screen, game_settings, hero, bullets, enemy1, tiles):
    for wall in tiles:
        screen.blit(wall.image, wall.rect)
    if pygame.sprite.spritecollideany(hero, tiles,):
        print("YES")

        

    else:
        hero.rect.y += 1

    if enemy1.lep:
        enemy1.draw_enemy()
        enemy1.update()
    if hero.make_jump:
        hero.jump(game_settings)
    hero.update(screen)
    for bullet in bullets:
        bullet.draw_bullet()
        if bullet.rect.y > 660:
            bullets.remove(bullet)
        if bullet.rect.x < hero.rect.x + 350:
            # bullet.trans()
            bullet.rect.x += 6
            bullet.rect.y -= 0.5
        elif bullet.rect.x != hero.rect.x + 500 and bullet.rotate_arrow:
            bullet.image = pygame.transform.rotate(bullet.image, -15)
            bullet.rotate_arrow = False
        elif bullet.rect.x != hero.rect.x + 500:
            bullet.rect.x += 6
            bullet.rect.y += 1
        if bullet.rect.x > enemy1.x and bullet.rect.y < enemy1.y + 200 and bullet.rect.y > enemy1.y:
             enemy1.lep = False
             enemy1.x = 0
             enemy1.y = 0
             bullets.remove(bullet)
    # hero.blitme()
