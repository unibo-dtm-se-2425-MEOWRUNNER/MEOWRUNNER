import pygame
import random
import os

from source.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN
from source.visuals import ROAD, ROCK, WATER, RUNNING, DUCKING, START
from source.cat import Cat
from source.obstacles import Water, Rock # here i need to finish the code in visuals with the obsticles

def main():
    global game_speed, x_pos_road, y_pos_road, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Cat()
    # cloud = Cloud() #we dont have cloud but i migth add
    game_speed = 20
    x_pos_road = 0
    y_pos_road = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf',20)
    obstacles = []
    death_count = 0

    def score ():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        
        text = font.render("Points:" + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
    
    def road():
        global x_pos_road, y_pos_road
        image_width = ROAD.get_width()
        SCREEN.blit(ROAD, (x_pos_road, y_pos_road))
        SCREEN.blit(ROAD, (image_width + x_pos_road, y_pos_road))
        if x_pos_road <= -image_width:
            SCREEN.blit(ROAD, (image_width + x_pos_road, y_pos_road))
            x_pos_road = 0
        x_pos_road -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        SCREEN.fill ((255, 255, 255))
        userInput = pygame.key.get_pressed()
        
        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Rock(ROCK)) 
            elif random.randint (0, 2) == 1:
                obstacles.append(Water(WATER))
            #elif random.randint (0, 2) == 2:
                #obstacles.append(bird(BIRD))
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles)
            if player.cat_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                #menu(death_count)
        
        road()

        # cloud.draw(SCREEN)
        # cloud.update(game_speed)

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0,0,0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0,0,0))
            score = font.render("Your Score:" + str(points), True, (0,0,0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(START, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu (death_count=0)
                                      

