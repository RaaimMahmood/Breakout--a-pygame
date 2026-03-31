# brick.py - Brick class for the Breakout game

import pygame
from settings import *

class Brick:
    def __init__(self, x, y, width, height, color, hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hp = hp
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, offset_x=0, offset_y=0):
        rect = self.rect.move(offset_x, offset_y)
        pygame.draw.rect(screen, self.color, rect)
        # Optional: draw HP text if >1
        if self.hp > 1:
            font = pygame.font.SysFont(None, SMALL_FONT_SIZE)
            text = font.render(str(self.hp), True, WHITE)
            screen.blit(text, (rect.centerx - text.get_width() // 2 + offset_x, rect.centery - text.get_height() // 2 + offset_y))

    def hit(self):
        self.hp -= 1
        return self.hp <= 0