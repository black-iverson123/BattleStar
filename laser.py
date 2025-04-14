import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """Class to manage lasers fired from the ship"""
    
    def __init__(self, ai_game):
        """_summary_: Initialize the laser and its starting position
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #create a laser rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        
        #start each new laser at the bottom of the ship
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #store the laser's position as a decimal value
        self.y = float(self.rect.y)
        self.left_laser = float(self.rect.y)
        self.right_laser = float(self.rect.y)
    
    def update(self):
        """_summary_: Move the laser up the screen
        """
        #update the decimal position of the laser
        self.y -= self.settings.laser_speed
        
        
        #update the rect position
        self.rect.y = self.y
    
    def draw_laser(self):
        """_summary_: Draw the laser to the screen
        """
        pygame.draw.rect(self.screen, self.settings.laser_colour, self.rect)
