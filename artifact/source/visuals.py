import pygame
import os
from source.config import VISUALS_DIR

pygame.init()

# animations cat
RUNNING = [pygame.image.load(os.path.join(VISUALS_DIR, "cat/cat_normal.png")),
           pygame.image.load(os.path.join(VISUALS_DIR, "cat/cat_walk.png"))]

JUMPING = pygame.image.load(os.path.join(VISUALS_DIR, "cat/cat_normal.png")) 

DUCKING = [pygame.image.load(os.path.join(VISUALS_DIR, "cat/cat_duck1.png")),
           pygame.image.load(os.path.join(VISUALS_DIR, "cat/cat_duck2.png"))]

# enviroment
ROCK = pygame.image.load(os.path.join(VISUALS_DIR, "obsticles/rock.png"))
WATER = pygame.image.load(os.path.join(VISUALS_DIR, "obsticles/water.png"))

ROAD = pygame.image.load(os.path.join(VISUALS_DIR, "other/line.png"))