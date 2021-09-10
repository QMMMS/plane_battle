import pygame as py
from random import randint

speed = 40


class SnakeGame(object):
    def __init__(self):
        py.init()
        py.display.set_caption("QMMMS贪吃蛇")
        self.caption = py.display.set_mode((500, 500))
        self.snake = Snake(self.caption)
        self.food = Food(self.caption)
        self.clock = py.time.Clock()
        self.font1 = py.font.SysFont('宋体', 30, True)
        self.score = 0

    def __event_handler(self):
        if self.snake.grow(self.food):
            self.score += 1
        for snake_block in self.snake.snake_blocks[1:]:
            if self.snake.snake_blocks[0] == snake_block:
                self.__game_over()
        for event in py.event.get():
            if event.type == py.QUIT:
                self.__game_over()
            if event.type == py.KEYDOWN:
                if self.snake.direction in [2, 3]:
                    if event.key == py.K_UP:
                        self.snake.direction = 0
                    elif event.key == py.K_DOWN:
                        self.snake.direction = 1
                else:
                    if event.key == py.K_LEFT:
                        self.snake.direction = 2
                    elif event.key == py.K_RIGHT:
                        self.snake.direction = 3

    def __show_score(self):
        surface1 = self.font1.render("score:" + str(self.score), True, [255, 255, 255])
        self.caption.blit(surface1, [20, 20])

    # def __move_snake(self):
    #     self.snake.move()

    def __game_over(self):
        py.quit()
        print("你的得分是：" + str(self.score))
        exit()

    def start_game(self):
        while 1:
            self.clock.tick(speed)
            self.__event_handler()
            self.snake.move()
            self.food.draw_food()
            self.__show_score()
            py.display.update()
            self.caption.fill((0, 0, 0))


class Snake(object):
    def __init__(self, screen):
        self.screen = screen
        self.direction = 3
        self.white = (255, 255, 255)
        self.snake_blocks = [[250, 250], [240, 250], [230, 250], [220, 250]]
        for snake_block in self.snake_blocks:
            py.draw.rect(self.screen, self.white, py.Rect(snake_block[0], snake_block[1], 10, 10))

    def move(self):
        if self.direction == 3:
            # for snake_block in self.snake_blocks:
            #     snake_block[0] += 10
            current_x = self.snake_blocks[0][0]
            current_y = self.snake_blocks[0][1]
            self.snake_blocks.insert(0, [current_x + 10, current_y])
            self.snake_blocks.pop()
        elif self.direction == 0:
            current_x = self.snake_blocks[0][0]
            current_y = self.snake_blocks[0][1]
            self.snake_blocks.insert(0, [current_x, current_y - 10])
            self.snake_blocks.pop()
        elif self.direction == 1:
            current_x = self.snake_blocks[0][0]
            current_y = self.snake_blocks[0][1]
            self.snake_blocks.insert(0, [current_x, current_y + 10])
            self.snake_blocks.pop()
        else:
            current_x = self.snake_blocks[0][0]
            current_y = self.snake_blocks[0][1]
            self.snake_blocks.insert(0, [current_x - 10, current_y])
            self.snake_blocks.pop()
        if self.snake_blocks[0][0] > 500:
            self.snake_blocks[0][0] = 0
        elif self.snake_blocks[0][0] < 0:
            self.snake_blocks[0][0] = 500
        elif self.snake_blocks[0][1] < 0:
            self.snake_blocks[0][1] = 500
        elif self.snake_blocks[0][1] > 500:
            self.snake_blocks[0][1] = 0
        for snake_block in self.snake_blocks:
            py.draw.rect(self.screen, self.white, py.Rect(snake_block[0], snake_block[1], 10, 10))

    def grow(self, target):
        if target.x == self.snake_blocks[0][0] and target.y == self.snake_blocks[0][1]:
            self.snake_blocks.append([self.snake_blocks[3][0], self.snake_blocks[3][1]])
            target.x = self.__give_a_random_num()[0]
            target.y = self.__give_a_random_num()[1]
            return True

    def __give_a_random_num(self):
        num1 = randint(0, 50) * 10
        num2 = randint(0, 50) * 10
        if [num1, num2] not in self.snake_blocks:
            return num1, num2
        else:
            self.__give_a_random_num()


class Food(object):
    def __init__(self, screen):
        self.x = randint(0, 50) * 10
        self.y = randint(0, 50) * 10
        self.white = (255, 255, 255)
        self.screen = screen

    def draw_food(self):
        py.draw.rect(self.screen, self.white, py.Rect(self.x, self.y, 10, 10))


if __name__ == '__main__':
    game = SnakeGame()
    game.start_game()
