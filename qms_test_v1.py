import pygame as py

py.init()
clock = py.time.Clock()
screen = py.display.set_mode((480, 700))
bg = py.image.load("./images/background.png")
hero = py.image.load("./images/me1.png")
screen.blit(bg, (0, 0))
screen.blit(hero, (175, 700))
hero_rect = py.Rect(175, 700, 102, 126)
py.display.update()
while True:
    clock.tick(120)
    event_list = py.event.get()
    if len(event_list) > 0:
        print(event_list)
    for event in event_list:
        if event.type == py.QUIT:
            py.quit()
            exit()
    if hero_rect.y < -126:
        hero_rect.y = 700
    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    py.display.update()
