# main.py - Main game loop for Breakout

import pygame
import sys
import random
from settings import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from sound import SoundManager

# Game states
START = 0
PLAYING = 1
GAME_OVER = 2
WIN = 3

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.small_font = pygame.font.SysFont(None, SMALL_FONT_SIZE)
        self.state = START
        self.score = 0
        self.sound = SoundManager()
        self.shake_frames = 0
        self.shake_offset_x = 0
        self.shake_offset_y = 0
        self.reset_game()

    def reset_game(self):
        self.paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70)
        self.bricks = self.create_bricks()
        self.score = 0
        self.shake_frames = 0
        self.shake_offset_x = 0
        self.shake_offset_y = 0

    def create_bricks(self):
        bricks = []
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = col * (BRICK_WIDTH + 5) + 35
                y = row * (BRICK_HEIGHT + 5) + 50
                color = BRICK_COLORS[row]
                hp = BRICK_HP[row]
                bricks.append(Brick(x, y, color, hp))
        return bricks

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.state == START:
                        self.state = PLAYING
                    elif self.state in [GAME_OVER, WIN]:
                        self.state = START
                        self.reset_game()

    def update(self):
        if self.state == PLAYING:
            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            ball_bounced_wall = self.ball.update()

            # Ball-paddle collision
            if self.ball.rect.colliderect(self.paddle.rect):
                self.ball.speed_y = -abs(self.ball.speed_y)
                # Adjust angle based on where it hits the paddle
                offset = (self.ball.rect.centerx - self.paddle.rect.centerx) / (self.paddle.width / 2)
                self.ball.speed_x = offset * 5
                self.sound.play('paddle')

            if ball_bounced_wall:
                self.sound.play('wall')

            # Ball-brick collision
            for brick in self.bricks[:]:
                if self.ball.rect.colliderect(brick.rect):
                    self.ball.speed_y = -self.ball.speed_y
                    if brick.hit():
                        self.bricks.remove(brick)
                        self.score += SCORE_PER_BRICK
                        # Increase ball speed slightly
                        self.ball.speed_x += BALL_SPEED_INCREASE if self.ball.speed_x > 0 else -BALL_SPEED_INCREASE
                        self.ball.speed_y += BALL_SPEED_INCREASE if self.ball.speed_y > 0 else -BALL_SPEED_INCREASE
                        self.shake_frames = int(SHAKE_DURATION * FPS / 1000)
                        self.sound.play('brick')
                    break

            # Update shake
            if self.shake_frames > 0:
                self.shake_offset_x = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
                self.shake_offset_y = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
                self.shake_frames -= 1
            else:
                self.shake_offset_x = 0
                self.shake_offset_y = 0

            # Check win condition
            if not self.bricks:
                self.state = WIN

            # Check lose condition
            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                self.state = GAME_OVER

    def draw(self):
        self.screen.fill(BLACK)

        if self.state == START:
            self.draw_start_screen()
        elif self.state == PLAYING:
            self.paddle.draw(self.screen, self.shake_offset_x, self.shake_offset_y)
            self.ball.draw(self.screen, self.shake_offset_x, self.shake_offset_y)
            for brick in self.bricks:
                brick.draw(self.screen, self.shake_offset_x, self.shake_offset_y)
            self.draw_score(self.shake_offset_x, self.shake_offset_y)
        elif self.state == GAME_OVER:
            self.draw_game_over_screen()
        elif self.state == WIN:
            self.draw_win_screen()

        pygame.display.flip()

    def draw_start_screen(self):
        title = self.font.render("Breakout", True, WHITE)
        start_text = self.small_font.render("Press SPACE to start", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

    def draw_game_over_screen(self):
        game_over = self.font.render("Game Over", True, RED)
        restart = self.small_font.render("Press SPACE to restart", True, WHITE)
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(game_over, (SCREEN_WIDTH // 2 - game_over.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    def draw_win_screen(self):
        win = self.font.render("You Win!", True, GREEN)
        restart = self.small_font.render("Press SPACE to restart", True, WHITE)
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(win, (SCREEN_WIDTH // 2 - win.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    def draw_score(self, offset_x=0, offset_y=0):
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10 + offset_x, 10 + offset_y))

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()