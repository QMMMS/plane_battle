import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
CEE = pygame.USEREVENT
HFE = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=2):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super(Background, self).__init__("./images/background.png", speed=1)
        if is_alt is True:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super(Enemy, self).__init__("./images/enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super(Enemy, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
            
            
class Bullet(GameSprite):
    def __init__(self):
        super(Bullet, self).__init__("./images/bullet1.png")
        self.speed = -4

    def update(self):
        super(Bullet, self).update()
        if self.rect.bottom < 0:
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super(Hero, self).__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullet1_group = pygame.sprite.Group()

    def fire(self):
        bullet1_1 = Bullet()
        bullet1_2 = Bullet()
        bullet1_1.rect.centerx = self.rect.centerx
        bullet1_1.rect.y = self.rect.y
        bullet1_2.rect.centerx = self.rect.centerx
        bullet1_2.rect.y = self.rect.y - 20
        self.bullet1_group.add(bullet1_1)
        self.bullet1_group.add(bullet1_2)
