import pygame
from pygame.sprite import Sprite
from dino_runner.components.menu import Menu

from dino_runner.utils.constants import (
    FLY_ICON, #Se implementa fly icon como intento de realizar una fly con los datos importadors
    FLY_TYPE,
    FLYING,
    RUNNING ,
    DEFAULT_TYPE,
    JUMPING,
    DUCKING,
    SHIELD_TYPE,
    DUCKING_SHIELD,
    RUNNING_SHIELD,
    JUMPING_SHIELD,
    DINO_DEAD,
    HAMMER_TYPE,
    JUMPING_HAMMER,
    RUNNING_HAMMER,
    DUCKING_HAMMER
    )
JUMPING_ACTION = "jumping"
RUNNING_ACTION = "running"
DUCKING_ACTION = "dunking"
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD,HAMMER_TYPE: DUCKING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD,HAMMER_TYPE: RUNNING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD,HAMMER_TYPE: JUMPING_HAMMER}

class Dinosaur(Sprite):
    Y_POS = 310
    X_POS =  80
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.jump_velocity = self.JUMP_VELOCITY   
        self.step = 0
        self.action = RUNNING_ACTION
        self.has_powe_up = False
        self.has_powe_up_time_up = 0

    def update(self, user_input):
        if self.action == RUNNING_ACTION:
            self.run()
        elif self.action == JUMPING_ACTION:
            self.jump()
        elif self.action == DUCKING_ACTION:
            self.duck()
   
        if user_input[pygame.K_UP] and self.action != JUMPING_ACTION:
            self.action = JUMPING_ACTION
        
        if user_input[pygame.K_DOWN] and self.action != JUMPING_ACTION:
            self.action = DUCKING_ACTION
      
        if self.step >= 9:
            self.step = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step //5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = RUNNING_ACTION
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS + 35
        self.action = RUNNING_ACTION
        self.step += 1

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.has_powe_up = True
        self.has_powe_up_time_up = power_up.start_time + (power_up.duration * 1000)
        self.type = power_up.type
        print(self.has_powe_up_time_up)

    def draw_active_power_up(self, screen):
        if self.has_powe_up:
            left_time = round (
                (self.has_powe_up_time_up - pygame.time.get_ticks()) / 1000, 2
            )
            if left_time >= 0:
                menu = Menu(screen)
                menu.draw(
                    screen,
                    f"{self.type.capitalize()} Time: {left_time}",
                    x = 950, y = 80
                )
            else:
                self.type = DEFAULT_TYPE
                self.has_powe_up = False
    
    def on_dino_death(self):
        self.image = DINO_DEAD