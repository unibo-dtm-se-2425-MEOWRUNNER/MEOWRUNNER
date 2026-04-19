import os
import pygame

# screen constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# dynamic path calculation
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VISUALS_DIR = os.path.join(BASE_DIR, "visuals")