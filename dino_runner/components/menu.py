import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    half_screen_width = SCREEN_WIDTH  // 2
    half_screen_height = SCREEN_HEIGHT // 2
    def __init__(self, message, screen):
        screen.fill((255, 255,255))
        self.font= pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def update(self,game):
        pygame.display.update()
        self.handle_menu_events(game)
    
    def handle_menu_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.executing = False
            elif event.type == pygame.KEYDOWN:
                game.run()
    
    def draw(self,screen):
        screen.blit(self.text,self.text_rect)
    
    def reset_screen_color(self,screen):
        screen.fill((255,255,255))

    def update_message(self,message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)
        

        
        
       