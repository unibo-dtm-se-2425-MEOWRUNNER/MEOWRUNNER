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

START = pygame.image.load(os.path.join(VISUALS_DIR, "cat/cat_start.png"))
DEAD = pygame.image.load(os.path.join(VISUALS_DIR, "cat/cat_dead.png"))

# enviroment
GAME_OVER = pygame.image.load(os.path.join(VISUALS_DIR, "other/game_over.png"))
BACKGROUND = pygame.image.load(os.path.join(VISUALS_DIR, "other/background.jpg"))

tree_og = pygame.image.load(os.path.join(VISUALS_DIR, "other/tree.png"))
original_width_t = tree_og.get_width()
original_height_t = tree_og.get_height()
scale_factor_t = 0.5
new_width_t = int(original_width_t * scale_factor_t)
new_height_t = int(original_height_t * scale_factor_t)

TREE = pygame.transform.scale(tree_og, (new_width_t, new_height_t))

# obsticles
GORGE = pygame.image.load(os.path.join(VISUALS_DIR, "obsticles/gorge.jpg"))

plant_og = pygame.image.load(os.path.join(VISUALS_DIR, "obsticles/plant.png"))
original_width_p = plant_og.get_width()
original_height_p = plant_og.get_height()
scale_factor_p = 0.5
new_width_p = int(original_width_p * scale_factor_p)
new_height_p = int(original_height_p * scale_factor_p)

PLANT = pygame.transform.scale(plant_og, (new_width_p, new_height_p))