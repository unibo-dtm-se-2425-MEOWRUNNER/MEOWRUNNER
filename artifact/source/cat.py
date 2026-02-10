class Cat:
    #positions
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.cat_duck = False
        self.cat_run = True
        self.cat_jump = False

        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS

    def update(self, userInput):
        if self.cat_duck:
            self.duck()
        if self.cat_run:
            self.run()
        if self.dino_jump:
            self.jump()
    
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