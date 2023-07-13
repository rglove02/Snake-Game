import pygame
from config import config


class Snake:
    def __init__(self, screen):
        self.x = config["game"]["width"]/2
        self.y = config["game"]["height"]/2
        self.screen = screen
        self.body = []
        self.length = 1

    def eatApple(self):
        self.length += 1

    def drawSnake(self):
        self.drawBody()
        return pygame.draw.rect(self.screen, config["colors"]["green"], (self.x, self.y, config["snake"]["width"],config["snake"]["height"]))
    
    def moveSnake(self, x_change, y_change):
        self.body.append([self.x, self.y])
        self.x += x_change * config["snake"]["speed"]
        self.y += y_change * config["snake"]["speed"]

        if len(self.body) > self.length - 1:
            self.body.pop(0)

    def drawBody(self):
        for i in range(len(self.body)):
            pygame.draw.rect(self.screen, config["colors"]["green"], (self.body[i][0], self.body[i][1], config["snake"]["width"],config["snake"]["height"]))


