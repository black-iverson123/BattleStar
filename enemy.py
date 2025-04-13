import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """_summary_: class to create an alien in the armada

    Args:
        Sprite (_type_): Parent class of this derived class
    """
    
    def __init__(self, ai_game):
        """_summary_: initialize alien and its starting point
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings        
        #loading imagefile for alien
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        
        #loading each alien near the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store exact location of alien horizontal position
        self.x = float(self.rect.x)
    

    def check_boundaries(self):
        """_summary_: return True if at screen edge
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def  update(self):
        """_summary_: Move enemy in both directions
        """
        self.x += (self.settings.enemy_speed * self.settings.armada_direction)
        self.rect.x = self.x
    
        