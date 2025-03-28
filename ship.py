import pygame

class Ship:
    """ Class to manage ship"""
    
    def __init__(self, ai_game):
        """_summary_: Initaialize the ship and it's starting position
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        
        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.jpg')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom 
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """_summary_: drawing ship at current location
        """
        self.screen.blit(self.image, self.rect)
    
    