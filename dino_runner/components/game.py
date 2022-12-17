import pygame
from dino_runner.components.menu  import Menu
from dino_runner.utils.constants import BG, DINO_START, FLY_ICON, FONT_STYLE, HAMMER_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,SHIELD_TYPE
from dino_runner.components.score import Score
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstaclesManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(FLY_ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.menu = Menu(self.screen)

        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.death_count = 0
        self.executing = False

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.score.points = 0
        self.game_speed = self.GAME_SPEED
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.playing = True
        self.game_speed = self.GAME_SPEED 
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups
        self.score.reset_score()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager.update(self.game_speed,self.score.points,self.player)       
        self.score.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player.draw_active_power_up(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
       
        
        if  self.death_count == 0:
            self.menu.draw(self.screen, 'Press any key to start ...')
            self.screen.blit(DINO_START, (half_screen_width - 50, half_screen_height - 140))
        else:
            self.menu.draw(self.screen, 'Game over. Press any key to restart.')
            self.menu.draw(self.screen, f'Your score: {self.score.points}', half_screen_width, 350)
            self.menu.draw(self.screen, f'Highest score: {self.score.MAX_POINT}', half_screen_width, 400)
            self.menu.draw(self.screen, f'Total deaths: {self.death_count}', half_screen_width, 450)
            self.screen.blit(DINO_START, (half_screen_width - 50, half_screen_height - 140))
        self.menu.update(self)
            
    def on_death(self,obstacles):
        has_shield = self.player.type == SHIELD_TYPE or self.player.type == HAMMER_TYPE
        if not has_shield:
            self.player.on_dino_death()
            self.death_count += 1
            self.playing = False
        elif self.player.type == HAMMER_TYPE:
            obstacles.pop()

        return not has_shield
        