import sys
import pygame
from settings import Settings
from battleship import Ship
from laser import Laser
from enemy import Alien
from time import sleep
from stats import Stats
from button import Button
from score import Scoreboard

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
        # create an instance to store game statistics
        # and create a scoreboard
        self.stats = Stats(self)
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.lasers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self._create_armada()
        
        #make play button
        self.play_button =Button(self, "Start game!!!")
        
        
    
    def run_game(self):
        """_summary_: game loop for the game is started
        """
        clock = pygame.time.Clock()
        while True:
            """start main loop for the game"""
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_lasers()
                self._update_enemies()
                self._big_shot()
                
            self._update_screen()
            #clock.tick(60) #limitting  game to a capped frame rate to avoid lagging
    
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """_summary_: Starts game upon clicking start game
        """
        clicked_button = self.play_button.rect.collidepoint(mouse_pos)
        if clicked_button and not self.stats.game_active:
            #Reset game settings
            self.settings.dynamic_settings()
            self._start_game()
            #Hide mouse cursor
            pygame.mouse.set_visible(False)
    
    def _start_game(self):
        """_summary_: game start commands
        """
        #Reset game stats
        self.stats.reset_stats()
        self.stats.game_active=True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
            
        #remove all remaining aliens and lasers
        self.enemies.empty()
        self.lasers.empty()
            
        #create a new armada and center battleship
        self._create_armada()
        self.ship.center_ship()
                
    def _check_keydown_events(self, event):
        """_summary__: checking for keypresses and moving the ship accordingly

        Args:
            event (_type_): type of event recorded by pygame event handler
        """
        if event.key == pygame.K_RIGHT:
            # move ship to the right
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            # move ship to the left
            self.ship.move_left = True
        if event.key == pygame.K_UP:
            # move ship upwards
            self.ship.move_up = True
        if event.key == pygame.K_DOWN:
            # move ship downwards
            self.ship.move_down = True
        if event.key == pygame.K_SPACE:
            self._fire_laser()
        if event.key == pygame.K_q:
            # quit game
            sys.exit()
        if event.key == pygame.K_d:
            now = pygame.time.get_ticks()
            if not self.settings.big_shot_active and (now - self.settings.big_shot_last_used) >= self.settings.big_shot_cooldown:
                self.settings.big_shot_active = True
                self.settings.big_shot_start_time = now
                self.settings.laser_colour = (255, 165, 0)
                self.settings.laser_width = 10
                self.settings.laser_height = 40
        if event.key == pygame.K_p:
            # start game
            self._start_game()
    
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
        """_summary_: Fire a laser from the ship"""
        if len(self.lasers) < self.settings.allowed_lasers:
            # Create a new laser with the current settings
            new_laser = Laser(self)
            self.lasers.add(new_laser)
            
            # Fire additional lasers from the wings when above level 3
            if self.stats.level >= 3:
                self.settings.laser_colour = (0, 0,255)
                if self.settings.big_shot_active:
                    self.settings.laser_colour = (255, 165, 0)
                left_laser = Laser(self)
                left_laser.rect.midtop = self.ship.rect.midleft
                self.lasers.add(left_laser)
                
                right_laser = Laser(self)
                right_laser.rect.midtop = self.ship.rect.midright
                self.lasers.add(right_laser)
            
    def _update_lasers(self):
        """_summary_: update position of lasers and removes old ones"""
        #updating laser position
        self.lasers.update()
        
        #removing lasers off screen
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)  
        
        self._check_laser_enemy_contact()
    
    def _big_shot(self):
        """_summary_: Activate or deactivate big shot based on timing."""
        if self.settings.big_shot_active:
            now = pygame.time.get_ticks()
            elapsed_time = now - self.settings.big_shot_start_time
            if elapsed_time >= self.settings.big_shot_duration:
                # Time's up: deactivate big shot
                self.settings.big_shot_active = False
                if self.stats.level >= 3:
                    self.settings.laser_colour = (0, 0, 255)
                self.settings.laser_width = 3
                self.settings.laser_height = 15
                self.settings.big_shot_last_used = now  # Start cooldown timer

                # Reset existing lasers to normal size and color
                for laser in self.lasers.sprites():
                    laser.rect.width = self.settings.laser_width
                    laser.rect.height = self.settings.laser_height

    def _check_laser_enemy_contact(self):
        """_summary_: Responds to laser-enemy collision
        """
         #Here a check for if any laser hit enemies
        #if true, remove enemy and laser
        collisions = pygame.sprite.groupcollide(self.lasers, self.enemies, True, True)
        
        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
            self.sb.prep_score()
            self.sb.check_best_score()
        
        if not self.enemies:
            #Remove existing laser and create a new armada
            self.lasers.empty()
            self._create_armada()
            self.settings.increase_speed()
            
            #increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def _create_armada(self):
        """_summary_: create a fleet of aliens
        """
        enemy = Alien(self)
        enemy_width, enemy_height = enemy.rect.size
        space_x = self.settings.screen_width - (2 * enemy_width)
        no_enemies_x = space_x // (2 * enemy_width)
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        space_y = (self.settings.screen_height -(3 * enemy_height) - ship_height)
        no_rows = space_y // (2 * enemy_height)
        # Create the full fleet of aliens.
        for row_number in range(no_rows):
            for enemy_number in range(no_enemies_x):
                self._create_enemy(enemy_number, row_number)
            
            
    def _create_enemy(self, enemy_no, row_number):
        """_summary_: create an enemy and place in row
        """
        enemy = Alien(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.x = enemy_width + 2 * enemy_width * enemy_no
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
        self.enemies.add(enemy)
    
    def _check_armada_edges(self):
        """_summary_: Gives best response if any alien has reached an edge
        """
        for enemy in self.enemies.sprites():
            if enemy.check_boundaries():
                self._change_armada_direction()
                break
        
    def _change_armada_direction(self):
        """_summary_: Drop the armada and changes direction
        """
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.armada_speed_drop
        self.settings.armada_direction *= -1
        
    def _update_enemies(self):
        """Update enemy position, checking if fleet is at screen 
           boundary then updated positions for all enemies in
           armada """
        self._check_armada_edges()
        self.enemies.update()
        
        # look for alien-player collision
        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self._ship_hit()
            
        #look for enemy reeaching the screen bottom
        self._check_enemy_at_bottom()
    
    def _ship_hit(self):
        """_summary_: Respond to the ship being hit by an enemy
        """
        if self.stats.ships_left > 0:
            #Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            #Get rid of any remainig enemies and lasers
            self.enemies.empty()
            self.lasers.empty()
            
            sleep(0.5)
            #create a new armada and center the battleship
            self._create_armada()
            self.ship.center_ship()
        else:
            self.stats.game_active=False
    
    def _check_enemy_at_bottom(self):
        """_summary_: Checking if enemies have reached bottom of screen
        """
        screen_rect = self.screen.get_rect()
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= screen_rect.bottom:
                #behave like ship has been hit
                self.enemies.empty()
                self.lasers.empty()
                
                self._create_armada()
                self.ship.center_ship()
                
    
    def _update_screen(self):
        """_summary_: Redraw the screen during each pass through the loop."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        self.enemies.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw()

        # Display "BIG SHOT ACTIVE!" message
        if self.settings.big_shot_active:
            font = pygame.font.SysFont(None, 15)
            text = font.render("BIG SHOT ACTIVE!!!", True, (255, 165, 0))
            self.screen.blit(text, (20, 60))

        # Display cooldown timer for big shot
        if not self.settings.big_shot_active and self.stats.game_active:
            cooldown_remaining = max(0, (self.settings.big_shot_cooldown - (pygame.time.get_ticks() - self.settings.big_shot_last_used)) // 1000)
            font = pygame.font.SysFont(None, 15)
            text = font.render(f"Big Shot Cooldown: {cooldown_remaining}s", True, (255, 165, 0))
            self.screen.blit(text, (20, 60))

        pygame.display.flip()
        
                
            
if __name__ == "__main__":
    ai =  AlienInvasion()
    ai.run_game()