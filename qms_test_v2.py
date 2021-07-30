import pygame as py
from plane_sprites import *

py.init()
clock = py.time.Clock()
screen = py.display.set_mode((480, 700))
bg = py.image.load("./images/background.png")
hero = py.image.load("./images/me1.png")
screen.blit(bg, (0, 0))
screen.blit(hero, (175, 700))
hero_rect = py.Rect(175, 700, 102, 126)

enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
enemy_group = py.sprite.Group(enemy1, enemy2)

py.display.update()
while True:
    clock.tick(120)
    event_list = py.event.get()
    for event in event_list:
        if event.type == py.QUIT:
            py.quit()
            exit()
    if hero_rect.y < -126:
        hero_rect.y = 700
    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)

    py.display.update()
