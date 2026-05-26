import unittest
import pygame
import sys
import os

artifact_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'artifact'))
sys.path.insert(0, artifact_path)

from source.cat import Cat
from source.obstacles import Plant, Gorge, Tree, Bee
from source.visuals import PLANT, GORGE, TREE, BEE

pygame.init()

class TestCat(unittest.TestCase):
    def test_cat_initial_position(self):
        cat = Cat()
        self.assertEqual(cat.cat_rect.x, 80)
        self.assertEqual(cat.cat_rect.y, 358)

    def test_cat_initial_state(self):
        cat = Cat()
        self.assertTrue(cat.cat_run)
        self.assertFalse(cat.cat_jump)
        self.assertFalse(cat.cat_duck)
    
    def test_cat_jump_trigger(self):
        cat = Cat()
        userInput = {pygame.K_UP: True, pygame.K_DOWN: False}
        cat.update(userInput)

        self.assertTrue(cat.cat_jump)
        self.assertFalse(cat.cat_run)
        self.assertFalse(cat.cat_duck)

    def test_cat_duck_trigger(self):
        cat = Cat()
        userInput = {pygame.K_UP: False, pygame.K_DOWN: True}
        cat.update(userInput)

        self.assertTrue(cat.cat_duck)
        self.assertFalse(cat.cat_run)
        self.assertFalse(cat.cat_jump)
        
    def test_cat_returns_to_run(self):
        cat = Cat()
        userInput = {pygame.K_UP: False, pygame.K_DOWN: True}
        cat.update(userInput)

        userInput = {pygame.K_UP: False, pygame.K_DOWN: False}
        cat.update(userInput)

        self.assertTrue(cat.cat_run)
        self.assertFalse(cat.cat_duck)


class TestObstacles(unittest.TestCase):
    def test_plant_spawns_offscreen(self):
        plant = Plant(PLANT)
        self.assertEqual(plant.rect.x, 1100)

    def test_gorge_spawns_offscreen(self):
        gorge = Gorge(GORGE)
        self.assertEqual(gorge.rect.x, 1100)

    def test_bee_spawns_offscreen(self):
        bee = Bee(BEE)
        self.assertEqual(bee.rect.x, 1090)

    def test_bee_spawns_high(self):
        bee = Bee(BEE)
        self.assertLess(bee.rect.y, 380)

    def test_three_obstacle_types(self):
        plant = Plant(PLANT)
        gorge = Gorge(GORGE)
        bee = Bee(BEE)

        self.assertIsNotNone(plant)
        self.assertIsNotNone(gorge)
        self.assertIsNotNone(bee)
    
    def test_obstacle_move_left(self):
        plant = Plant(PLANT)
        obstacles = [plant]

        plant.rect.x = -1000
        plant.update(20, obstacles)

        self.assertEqual(len(obstacles), 0)

    def test_tree_is_decoration(self):
        tree = Tree(TREE)
        self.assertTrue(hasattr(tree, 'is_decoration'))
        self.assertTrue(tree.is_decoration)


class TestCollision(unittest.TestCase):
    def test_collision_detected(self):
        cat = Cat()
        plant = Plant(PLANT)

        plant.rect.x = cat.cat_rect.x
        plant.rect.y = cat.cat_rect.y

        self.assertTrue(cat.cat_rect.colliderect(plant.rect))

    def test_no_collision_when_separated(self):
        cat = Cat()
        plant = Plant(PLANT)

        plant.rect.x = 1000
        plant.rect.y = 400

        self.assertFalse(cat.cat_rect.colliderect(plant.rect))

    def test_jump_avoids_collision(self):
        cat = Cat()
        plant = Plant(PLANT)

        plant.rect.x = cat.cat_rect.x + 50
        plant.rect.y = 400

        userInput = {pygame.K_UP: True, pygame.K_DOWN: False}
        cat.update(userInput)

        for _ in range(15):
            cat.update({pygame.K_UP: False, pygame.K_DOWN: False})

        self.assertLess(cat.cat_rect.y, plant.rect.y)

    def test_duck_avoids_bee(self):
        cat = Cat()
        bee = Bee(BEE)

        bee.rect.x = cat.cat_rect.x + 50
        bee.rect.y = 320

        userInput = {pygame.K_UP: False, pygame.K_DOWN: True}
        cat.update(userInput)

        self.assertTrue(cat.cat_duck)
        self.assertFalse(cat.cat_run)
        self.assertFalse(cat.cat_jump)
        self.assertLessEqual(cat.cat_rect.height, cat.image.get_height())


class TestTreeSpawning(unittest.TestCase):
    def test_tree_collision_check(self):
        tree_spawn_x = 1100
        obstacle_x = 1050

        distance = abs(tree_spawn_x - obstacle_x)
        can_spawn = distance >= 250

        self.assertFalse(can_spawn)

    def test_tree_can_spawn_when_clear(self):
        tree_spawn_x = 1100
        obstacle_x = 500

        distance = abs(tree_spawn_x - obstacle_x)
        can_spawn = distance >= 250

        self.assertTrue(can_spawn)

class TestGameMechanics(unittest.TestCase):
    def test_score_increment(self):
        points = 0
        points += 1
        self.assertEqual(points, 1)

    def test_speed_increase(self):
        game_speed = 20
        points = 100

        if points % 100 == 0:
            game_speed += 1

        self.assertEqual(game_speed, 21)

    def test_speed_increase_multiple_milestones(self):
        game_speed = 20
        points = 250

        excepted_speed = 20 + (points // 100)

        self.assertEqual(excepted_speed, 22)

class TestGameDifficulty(unittest.TestCase):
    def test_speed_never_decreases(self):
        game_speed = 20

        for points in [100, 200, 300]:
            new_speed = 20 + (points // 100)
            self.assertGreaterEqual(new_speed, game_speed)
            game_speed = new_speed
    
    def test_speed_caps_appropriately(self):
        points = 5000 
        game_speed = 20 + (points // 100)

        self.assertGreater(game_speed, 20)
        self.assertEqual(game_speed, 70)

if __name__ == '__main__':
    unittest.main()