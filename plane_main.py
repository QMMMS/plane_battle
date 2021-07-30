import pygame as py
from plane_sprites import *

FPS = 60  # 如果你想修改帧率，可将60改为其他数(可能会使难度变化)
EPS = 0.5  # 如果你想修改敌机出场频率，修改此处（EPS越小，敌机越多）
BFS = 0.5  # 如果你想修改子弹出现频率，修改此处（BPS越小，子弹越多）


class PlaneGame(object):
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode(SCREEN_RECT.size)
        self.clock = py.time.Clock()
        self.__create_sprites()
        py.time.set_timer(CEE, int(EPS * 1000))
        py.time.set_timer(HFE, int(BFS * 1000))

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = py.sprite.Group(bg1, bg2)
        self.enemy_group = py.sprite.Group()
        self.hero = Hero()
        self.hero_group = py.sprite.Group(self.hero)

    def __event_handler(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.__game_over()
            elif event.type == CEE:
                enemy1 = Enemy()
                self.enemy_group.add(enemy1)
            elif event.type == HFE:
                self.hero.fire()
        keys_pressed = py.key.get_pressed()
        if keys_pressed[py.K_RIGHT]:
            if self.hero.rect.x < 378:
                self.hero.rect.x += 3
        elif keys_pressed[py.K_LEFT]:
            if self.hero.rect.x > 0:
                self.hero.rect.x -= 3
        elif keys_pressed[py.K_UP]:
            if self.hero.rect.y > 0:
                self.hero.rect.y -= 3
        elif keys_pressed[py.K_DOWN]:
            if self.hero.rect.y < 574:
                self.hero.rect.y += 3

    def __check_collide(self):
        py.sprite.groupcollide(self.hero.bullet1_group,
                               self.enemy_group, True, True)
        if py.sprite.groupcollide(self.hero_group,
                                  self.enemy_group, True, True):
            self.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero.bullet1_group.update()
        self.hero.bullet1_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        py.quit()
        exit()

    def start_game(self):
        while True:
            self.clock.tick(FPS)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            py.display.update()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
