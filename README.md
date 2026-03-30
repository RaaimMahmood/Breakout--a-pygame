# Breakout Game

A classic Breakout (Arkanoid-style) game implemented in Python using Pygame.

## Features

- Classic paddle and ball gameplay
- Multiple rows of bricks with different colors and hit points
- Score tracking
- Win and lose conditions
- Increasing difficulty (ball speed increases with each brick hit)
- Sound effects for collisions
- Screen shake effect on brick destruction
- Clean, modular code structure

## Installation

1. Ensure you have Python 3.6+ installed.
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Clone or download this repository.

## How to Run

Run the game using:
```
python main.py
```

## Controls

- **Left Arrow** or **A**: Move paddle left
- **Right Arrow** or **D**: Move paddle right
- **Space**: Start game / Restart after game over

## Game Rules

- Control the paddle to bounce the ball and destroy all bricks.
- Each brick destroyed gives you 10 points.
- If the ball falls below the paddle, you lose.
- Destroy all bricks to win!
- Ball speed increases slightly with each brick hit for added challenge.

## Project Structure

- `main.py`: Main game loop and state management
- `paddle.py`: Paddle class
- `ball.py`: Ball class
- `brick.py`: Brick class
- `settings.py`: Game constants and configuration
- `sound.py`: Sound management
- `assets/sounds/`: Directory for sound files (paddle.wav, wall.wav, brick.wav)
- `README.md`: This file

## Dependencies

- Pygame

## License

This project is open source. Feel free to use and modify.