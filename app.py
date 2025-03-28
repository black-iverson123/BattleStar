import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """_summary_: class to create, manage assets and game behaviour
    """
    
    def __init__(self):
        """_summary_: game and resources initialized
        """
        pygame.init()
        self.settings=Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship=Ship(self)
        
        
    
    def run_game(self):
        """_summary_: game loop for the game is started
        """
        while True:
            #for keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            # redrawing the screen during each pass through the loop
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()
                    
            # to make most recently drawn screen visible
            pygame.display.flip()
            
if __name__ == "__main__":
    ai =  AlienInvasion()
    ai.run_game()