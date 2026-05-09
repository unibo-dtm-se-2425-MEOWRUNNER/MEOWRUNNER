import random
import pygame
from source.config import SCREEN_WIDTH

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        full_rect = self.image.get_rect()
        self.rect = pygame.Rect(
            SCREEN_WIDTH,
            0,
            full_rect.width + 5,
            full_rect.height - 50
        )
        self.image_y = 0

    def update (self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x <- self.rect.width:
            obstacles.pop(0)
    
    def draw(self, SCREEN, debug=False):
        SCREEN.blit(self.image, (self.rect.x, self.image_y))
        
        if debug:
            pygame.draw.rect(SCREEN, (255, 0, 0), self.rect, 2)


class Plant(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.image_y = 382
        self.rect.y = 380

class Gorge(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 420
        self.image_y = 430

class Tree(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 300
        self.image_y = 220
        self.is_decoration = True

    def draw(self, SCREEN, debug = False):
        SCREEN.blit(self.image, (self.rect.x, self.image_y))

class Bee(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 350
        self.image_y = 350

        self.rect.width += 20
        self.rect.height += 30
        self.rect.x -= 10