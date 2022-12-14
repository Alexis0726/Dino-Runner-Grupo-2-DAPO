from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS
import pygame

class ObstaclesManager:
    def __init__(self):
        self.obstacles: list[Obstacle]= []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
       
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)