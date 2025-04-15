import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Class to manage ship"""
    
    def __init__(self, ai_game):
        """_summary_: Initaialize the ship and it's starting position
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        
        #load the ship image and get its rect
        self.image = pygame.image.load('assets/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom 
        self.rect.midbottom = self.screen_rect.midbottom
        
        # storing a decimal value for ship's horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # #movement flags
        self.move_right = False 
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def blitme(self):
        """_summary_: drawing ship at current location
        """
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """_summary_: center battleship on the screen
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    def update(self):
        #updating ship position based on movement flags
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.move_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
    
    