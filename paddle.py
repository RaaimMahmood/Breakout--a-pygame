# paddle.py - Paddle class for the Breakout game

import pygame
from settings import *

class Paddle:
    def __init__(self, x, y, screen_width):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = PADDLE_SPEED
        self.color = PADDLE_COLOR
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, keys):
        # Move left
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed
        # Move right
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < self.screen_width:
            self.rect.x += self.speed

    def draw(self, screen, offset_x=0, offset_y=0):
        rect = self.rect.move(offset_x, offset_y)
        pygame.draw.rect(screen, self.color, rect)