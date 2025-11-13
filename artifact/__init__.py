import logging
import os
import sys
import random
import pygame

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('artifact')

pygame.init()

screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))

cat_start = pygame.image.load(os.path.join("visuals/cat", "cat_start.png"))
running = [pygame.image.load(os.path.join("visuals/cat", "cat_normal.png")),
           pygame.image.load(os.path.join("visuals/cat", "cat_walk.png"))]
jumping = pygame.image.load(os.path.join("visuals/cat", "cat_normal.png"))
# i wanted to add another function with sound + also sounds for colisions

rock = pygame.image.load(os.path.join("visuals/obsticles", "rock.png"))
water = pygame.image.load(os.path.join("visuals/obsticles", "water.png"))

road = pygame.image.load(os.path.join("visuals/other", "line.png"))

# this is the initial module of your app
# this is executed whenever some client-code is calling `import artifact` or `from artifact import ...`
# put your main classes here, eg:
class MyClass:
    def my_method(self):
        return "Hello World"


def main():
    # this is the main module of your app
    # it is only required if your project must be runnable
    # this is the script to be executed whenever some users writes `python -m artifact` on the command line, eg.
    x = MyClass().my_method()
    print(x)


# let this be the last line of this file
logger.info("artifact loaded")
