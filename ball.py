# ball.py - Ball class for the Breakout game

import pygame
from settings import *

class Ball:
    def __init__(self, x, y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = BALL_RADIUS
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
        self.color = BALL_COLOR
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.center = (self.x, self.y)
        bounced = False

        # Bounce off left and right walls
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x = -self.speed_x
            bounced = True

        # Bounce off top wall
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y
            bounced = True

        return bounced

    def draw(self, screen, offset_x=0, offset_y=0):
        pygame.draw.circle(screen, self.color, (self.x + offset_x, self.y + offset_y), self.radius)

    def reset(self, paddle):
        self.x = paddle.rect.centerx
        self.y = paddle.rect.top - self.radius
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
        self.rect.center = (self.x, self.y)