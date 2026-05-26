import pygame
import random
import os

from source.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN
from source.visuals import START, DEAD, GAME_OVER, BACKGROUND, GORGE, PLANT, TREE, BEE
from source.obstacles import Gorge, Plant, Tree, Bee
from source.cat import Cat

DEBUG_MODE = False  # set to False to hide collision boxes

def main():
    global game_speed, x_pos_road, y_pos_road, points, obstacles
    run = True 
    clock = pygame.time.Clock()
    player = Cat()
    game_speed = 20
    x_pos_road = 0
    y_pos_road = 432
    points = 0
    font = pygame.font.Font('freesansbold.ttf',20)
    obstacles = []
    trees = []
    tree_spawn_timer = 0
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
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        background_scaled = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.blit(background_scaled, (0, 0))
        userInput = pygame.key.get_pressed()
        
        collision = False
        for obstacle in obstacles:
            if player.cat_rect.colliderect(obstacle.rect):
                collision = True
                break
        
        for tree in trees:
            tree.draw(SCREEN, debug=False)
            tree.update(game_speed, trees)

        if collision:
            player.image = DEAD
            player.draw(SCREEN, debug=DEBUG_MODE)
            game_over_rect = GAME_OVER.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-100))
            SCREEN.blit(GAME_OVER, game_over_rect)
        else:
            player.update(userInput)
            player.draw(SCREEN, debug=DEBUG_MODE)
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN, debug=DEBUG_MODE)
            obstacle.update(game_speed, obstacles)

        tree_spawn_timer += 1
        if tree_spawn_timer > random.randint(40, 80):
            can_spawn_tree = True

            if len(obstacles) == 0: 
                can_spawn_tree = False

            if can_spawn_tree:
                trees.append(Tree(TREE))

            tree_spawn_timer = 0 

        if len(obstacles) == 0:
            rand_choice = random.randint(0,2)
            if rand_choice == 0:
                obstacles.append(Plant(PLANT))
            elif rand_choice == 1:
                obstacles.append(Gorge(GORGE))
            else:
                obstacles.append(Bee(BEE))
        
        

             #for obstacle in obstacles:
                 #if isinstance(obstacle, Gorge):
                     #if abs(obstacle.rect.x - SCREEN_WIDTH)< 250:
                         #can_spawn_tree = False
                         #break  
            
                    

        if collision:
            pygame.display.update()
            pygame.time.delay(1000)    
            death_count += 1
            menu(death_count)             
        
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

menu(death_count=0)
                                      

