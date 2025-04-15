import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """_summary_: Create and initialize button attributes
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #set the button properties
        self.width, self.height = 500, 50
        self.button_colour = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("verdona", 40)
        
        #Build button object and centering
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #The button message to be made once
        self._prep_msg(msg) 
    
    def _prep_msg(self, msg):
        """_summary_: msg is turned to a rendered image and center text on button
        """
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw(self):
        #Draw blank buton and then draw message
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        