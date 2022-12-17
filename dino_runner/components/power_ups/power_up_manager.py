import pygame
from random import randint
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.power_up import PowerUp



class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if not self.power_ups and self.when_appears == score:
            self.power_ups.append(Shield())
            self.when_appears += randint(200, 300)

    def update(self, game_speed, score, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if power_up.rect.colliderect(player.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up)
                self.power_ups.pop()
                print("power")

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_up(self):
        self.power_ups = []
        self.when_appears = randint(300, 500)
        