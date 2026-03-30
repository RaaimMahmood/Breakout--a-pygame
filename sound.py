# sound.py - Sound management for the Breakout game

import pygame
from settings import *

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        sound_files = {
            'paddle': PADDLE_SOUND,
            'wall': WALL_SOUND,
            'brick': BRICK_SOUND
        }
        for name, path in sound_files.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(path)
                self.sounds[name].set_volume(SOUND_VOLUME)
            except (pygame.error, FileNotFoundError):
                print(f"Warning: Could not load sound file {path}. Sound effect '{name}' will be skipped.")
                self.sounds[name] = None

    def play(self, sound_name):
        if sound_name in self.sounds and self.sounds[sound_name]:
            self.sounds[sound_name].play()