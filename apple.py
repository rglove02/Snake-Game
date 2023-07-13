import pygame
from config import config
import random

class Apple:
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.randomize()
        self.screen = screen

    def randomize(self):
        self.x = random.randint(config["game"]["bumper_size"],config["game"]["width"]-(config["game"]["bumper_size"] * 2))
        self.y = random.randint(config["game"]["bumper_size"],config["game"]["height"]-(config["game"]["bumper_size"] * 2))

    def drawApple(self):
        return pygame.draw.rect(self.screen, config["colors"]["apple-red"], (self.x, self.y, config["apple"]["width"],config["apple"]["height"]))