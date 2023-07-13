import pygame
import time
from snake import Snake
from apple import Apple
from config import config

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.snake = Snake(screen)
        self.apple = Apple(screen)
        self.fps_clock = pygame.time.Clock()

    def gameLoop(self):
        quitVar = False
        x_change = 0
        y_change = 0
        while quitVar == False:
            self.screen.fill(config["colors"]["red"])
            box = pygame.draw.rect(self.screen, config["colors"]["black"], (config["game"]["bumper_size"],config["game"]["bumper_size"], config["game"]["width"]-(config["game"]["bumper_size"]*2), config["game"]["height"]-(config["game"]["bumper_size"]*2)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitVar = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        y_change = 0
                        x_change = -1
                    elif event.key == pygame.K_RIGHT:
                        y_change = 0
                        x_change = 1
                    if event.key == pygame.K_UP:
                        y_change = -1
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = 1
                        x_change = 0

            self.snake.moveSnake(x_change,y_change)
            snakeRect = self.snake.drawSnake()
            appleRect = self.apple.drawApple()

            if snakeRect.colliderect(appleRect):
                self.apple.randomize()
                self.snake.eatApple()
                self.score += 1
                
            if not snakeRect.colliderect(box):
                quitVar = True
                
                font = pygame.font.SysFont("Arial", 40)
                text = font.render("Game Over", True, config["colors"]["red"])
                self.screen.blit(text,(200,200))
                pygame.display.update()
                time.sleep(10)
        
            self.fps_clock.tick(config["game"]["fps"])
            pygame.display.update()
        
        pygame.quit()
                    
