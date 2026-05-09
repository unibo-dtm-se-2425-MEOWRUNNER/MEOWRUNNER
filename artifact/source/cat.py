import pygame
from source.visuals import DUCKING, RUNNING, JUMPING 

class Cat:
    #positions
    X_POS = 80
    Y_POS = 358    
    Y_POS_DUCK = 365
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.cat_duck = False
        self.cat_run = True
        self.cat_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS

    def update(self, userInput):
        if self.cat_duck:
            self.duck()
        if self.cat_run:
            self.run()
        if self.cat_jump:
            self.jump()
        
        if self.step_index >= 10:
            self.step_index = 0
    
        # If UP is pressed and we aren't already jumping -> JUMP
        if userInput [pygame.K_UP] and not self.cat_jump:
            self.cat_duck = False
            self.cat_run = False
            self.cat_jump = True

        # If DOWN is pressed and we aren't jumping -> DUCK
        elif userInput [pygame.K_DOWN] and not self.cat_jump:
            self.cat_duck = True
            self.cat_run = False
            self.cat_jump = False

        # If nothing is pressed -> RUN
        elif not (self.cat_jump or userInput[pygame.K_DOWN]):
            self.cat_duck = False
            self.cat_run = True
            self.cat_jump = False   

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        original_height = self.image.get_height()

        self.cat_rect.x = self.X_POS
        self.cat_rect.width = self.image.get_width()
        self.cat_rect.height = original_height - 30
        self.cat_rect.y = self.Y_POS_DUCK + 15

        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.cat_jump:
            self.cat_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <- self.JUMP_VEL:
            self.cat_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw (self, SCREEN, debug=False):
        if self.cat_duck:
            SCREEN.blit(self.image, (self.X_POS, self.Y_POS_DUCK))
        else:
            SCREEN.blit(self.image, (self.cat_rect.x, self.cat_rect.y))

        if debug:
            pygame.draw.rect(SCREEN, (0, 255, 0), self.cat_rect, 2)      