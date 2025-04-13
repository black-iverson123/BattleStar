import sys
import pygame
from settings import Settings
from ship import Ship
from laser import Laser

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
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.lasers = pygame.sprite.Group()
        
        
    
    def run_game(self):
        """_summary_: game loop for the game is started
        """
        while True:
            """start main loop for the game"""
            self._check_events()
            self.ship.update()
            self.lasers.update()
            self._update_lasers()
            self._update_screen()
            


    
    def _check_events(self):
            #listening and checking for exit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #end game
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    #checking for keypresses
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    #checking for key releases
                    self._check_keyup_events(event)
                

                        
    def _check_keydown_events(self, event):
        """_summary__: checking for keypresses and moving the ship accordingly

        Args:
            event (_type_): type of event recorded by pygame event handler
        """
        if event.key == pygame.K_RIGHT:
            #move ship to the right
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            #move ship to the left
            self.ship.move_left = True
        if event.key == pygame.K_UP:
            #move ship upwards
            self.ship.move_up = True
        if event.key == pygame.K_DOWN:
            #move ship downwards
            self.ship.move_down =True
        if event.key == pygame.K_SPACE:
            self._fire_laser()
        if event.key == pygame.K_q:
            #quit game
            sys.exit()
    
    def _check_keyup_events(self, event):
        """_summary__: checking for key releases and stopping the ship accordingly

        Args:
            event (_type_): type of event recorded by pygame event handler
        """
        if event.key == pygame.K_RIGHT:
            #stoping right movement
            self.ship.move_right = False 
        if event.key == pygame.K_LEFT:
            #stopping left movement
            self.ship.move_left = False 
        if event.key == pygame.K_UP:
            #stopping upward movement
            self.ship.move_up = False
        if event.key ==  pygame.K_DOWN:
            #stopping downward movement
            self.ship.move_down = False
        
    def _fire_laser(self):
        """_summary_: firing a laser from the ship
        """
        #create a new laser and add it to the lasers group
        if len(self.lasers) < self.settings.allowed_lasers:
            new_laser = Laser(self)
            self.lasers.add(new_laser)
        
    def _update_lasers(self):
        """update position of lasers and removes old ones"""
        #updating laser position
        self.lasers.update()
        
        #removing lasers off screen
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)  
                
    def _update_screen(self):
            # redrawing the screen during each pass through the loop
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()
            for laser in self.lasers.sprites():
                laser.draw_laser()
                    
            # to make most recently drawn screen visible
            pygame.display.flip()
        
                
            
if __name__ == "__main__":
    ai =  AlienInvasion()
    ai.run_game()