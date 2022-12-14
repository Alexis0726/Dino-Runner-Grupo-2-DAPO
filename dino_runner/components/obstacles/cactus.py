from pygame import Surface
from random import randint
from dino_runner.components.obstacles.obstacles import Obstacle


class Cactus(Obstacle):
    def __init__(self, images: list[Surface]):
        cactus_type = randint(0, 2)
        super().__init__(images[cactus_type])
        self.rect.y = 325