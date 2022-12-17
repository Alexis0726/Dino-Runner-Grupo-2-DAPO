from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, DINO_DEAD
import random
import pygame

class ObstaclesManager:
    def __init__(self):
        self.obstacles: list[Obstacle]= []

    def update(self, game_speed,player, on_death):
        self.random = random.randint(0, 1)

        if len(self.obstacles) == 0 and self.random == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        elif len(self.obstacles) == 0 and self.random == 1:
            self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect) and  on_death(self.obstacles):
                player.image = DINO_DEAD
                pygame.time.delay(2000)
                

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []