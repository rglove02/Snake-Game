import pygame
from game import Game
from config import config
        
pygame.init()
pygame.display.set_caption(config["game"]["caption"])
screen = pygame.display.set_mode((config["game"]["width"],config["game"]["height"]))

myGame = Game(screen)
myGame.gameLoop()

