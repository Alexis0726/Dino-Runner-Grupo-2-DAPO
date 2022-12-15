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
#1
        self.text1 = self.font.render(message, True, (255,255,255))
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = (self.half_screen_width, self.half_screen_height + 50)

        self.text2 = self.font.render(message, True, (255,255,255))
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = (self.half_screen_width, self.half_screen_height + 50)

        self.text3 = self.font.render(message, True, (255,255,255))
        self.text_rect3 = self.text3.get_rect()
        self.text_rect3.center = (self.half_screen_width, self.half_screen_height + 50)


   

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
        screen.blit(self.text1,self.text_rect1)
        screen.blit(self.text2,self.text_rect2)
        screen.blit(self.text3,self.text_rect3)
    
    def reset_screen_color(self,screen):
        screen.fill((255,255,255))

    def update_message(self,message, message1, message2, message3 ):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

        self.text1 = self.font.render(message1, True, (0,0,0))
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = (self.half_screen_width, self.half_screen_height + 50)

        self.text2 = self.font.render(message2, True, (0,0,0))
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = (self.half_screen_width, self.half_screen_height + 80)

        self.text3 = self.font.render(message3, True, (0,0,0))
        self.text_rect3 = self.text3.get_rect()
        self.text_rect3.center = (self.half_screen_width, self.half_screen_height + 110)

        
        
       