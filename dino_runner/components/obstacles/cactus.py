from pygame import Surface
from random import randint
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import SCREEN_HEIGHT


class Cactus(Obstacle):
    def __init__(self, images: list[Surface]):
        cactus_type = randint(0, 2)
        super().__init__(images[cactus_type])
        self.rect.y = (SCREEN_HEIGHT-self.rect.h)-204 
        