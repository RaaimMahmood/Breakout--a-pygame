# settings.py - Game constants and configuration
import os
import pygame

# Screen settings
SCREEN_WIDTH = 810
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 5
PADDLE_COLOR = WHITE

# Ball settings
BALL_RADIUS = 8
BALL_SPEED_X = 4
BALL_SPEED_Y = -4
BALL_COLOR = WHITE

# Brick settings
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
BRICK_HP = [1, 1, 2, 2, 3, 3]  # Hit points for each row

# Game settings
SCORE_PER_BRICK = 10
BALL_SPEED_INCREASE = 0.1

# Font settings
FONT_SIZE = 36
SMALL_FONT_SIZE = 24

# Sound settings
SOUND_VOLUME = 1.0  # 0.0 to 1.0

# Base directory (location of this settings.py file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute sound paths
PADDLE_SOUND = os.path.join(BASE_DIR, "assets", "sounds", "paddle.wav")
WALL_SOUND   = os.path.join(BASE_DIR, "assets", "sounds", "wall.wav")
BRICK_SOUND  = os.path.join(BASE_DIR, "assets", "sounds", "brick.wav")

# Screen shake settings
SHAKE_INTENSITY = 3  # pixels
SHAKE_DURATION = 200  # milliseconds