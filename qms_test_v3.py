import pygame as py
from plane_sprites import *
"""
这个测试文件是有错误的
主要是while循环的问题
还有，在PlaneGame封装的方法有些没有用到
懒得改
"""


FPS = 30


class PlaneGame(object):
    def __init__(self):
        self.screen = py.display.set_mode(SCREEN_RECT.size)
        self.clock = py.time.Clock()

    def __create_sprites(self):
        bg1 = GameSprite("./images/background.png")
        self.back_group = py.sprite.Group(bg1)
        Background("./images/background.png")
        enemy1 = GameSprite("./images/enemy1.png")
        enemy2 = GameSprite("./images/enemy1.png", 2)
        self.enemy_group = py.sprite.Group(enemy1, enemy2)

    def __event_handler(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        py.quit()
        exit()

    def start_game(self):
        while True:
            self.clock.tick(FPS)
            self.__event_handler()
            self.__check_collide()
            bg = py.image.load("./images/background.png")
            hero_rect = py.Rect(175, 700, 102, 126)

            self.screen.blit(bg, hero_rect)
            py.display.update()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
