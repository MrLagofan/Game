import pygame, sys, os
from settings import Settings
from robin_hood import Robin_hood
import game_functions as g_f
from pygame.sprite import Group
from enemy import Enemy
from tile import Tile


clock = pygame.time.Clock()


def init_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    bullets = Group()
    hero = Robin_hood(screen, game_settings)
    pygame.display.set_caption("The best game in the world")
    bg = pygame.image.load("img/_12_background.png").convert()
    bg = pygame.transform.scale(bg, (1600, 900))
    enemy1 = Enemy(screen, game_settings)

    tiles = Group()
    level1 = ["mmmmm",
              "mmmmmmmmm"
              "mmmmm",
              "mmmm",
              "mmmmm",
              "mmmmm",
              "",
              "",
              "",
              "",
              '',
              "ZmmmgmgmmZmmma",
              "bbbbbbbbbbbbbbbbbbbbbbbbbb",
              ]
    x = y = 0
    for row in level1:
        for col in row:
            if col == "Z":
                Tile(x, y, "box.png", tiles)
            elif col == "a":
                Tile(x, y, "barrel.png", tiles)
            elif col == "b":
                Tile(x, y, "block.png", tiles)

            elif col == "g":
                Tile(x, y, "grass.png", tiles)


            x += 64
        y += 64
        x = 0

    while True:
        g_f.check_events(hero, game_settings, bullets, screen)
        g_f.update_screen(screen, game_settings, hero, bullets, enemy1,tiles)
        #screen.blit(bg, (0 - game_settings.CameraX, 0 - game_settings.CameraY))
        screen.blit(hero.image, (hero.rect.x + game_settings.CameraX, hero.rect.y + game_settings.CameraY))
        pygame.display.flip()
        rel_x = x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < game_settings.width:
            screen.blit(bg, (rel_x, 0))
        x = 0 - hero.rect.x
        clock.tick(60)

init_game()