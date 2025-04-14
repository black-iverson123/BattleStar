class Settings:
    """_summary_: A class to keep game settings
    """
    
    def __init__(self):
        """_summary_: game settings initialized
        """
        #Screen settings
        self.screen_width = 650
        self.screen_height = 700
        self.bg_colour = (230, 230, 230)
        
        #ship settings
        self.ship_limit = 3
        
        #laser settings
        self.laser_width = 3
        self.laser_height = 15
        self.laser_colour = (255, 0, 0)
        self.allowed_lasers = 3
        self.big_shot_active = False
        self.big_shot_start_time = 0
        self.big_shot_last_used = 0
        self.big_shot_duration = 30_000  # 30 seconds in ms
        self.big_shot_cooldown = 30_000  # 30 seconds in ms

        #enemy settings
        self.armada_speed_drop = 10
        
        #Quickly speed up game 
        self.speed_scale = 1.1
        
        # enemy point value increase
        self.score_scale = 1.5
        
        self.dynamic_settings()
    
    def dynamic_settings(self):
        """_summary_: Initialize settings throughout the game"""
        self.ship_speed = 1.5
        self.laser_speed = 3.0
        self.enemy_speed = 0.5
        
        # Reset big shot settings
        self.big_shot_active = False
        self.big_shot_start_time = 0
        
        # Armada direction of 1 means right, -1 means left
        self.armada_direction = 1
        self.enemy_points = 50
        self.time = 30
        
    def increase_speed(self):
        """_summary_: increase speed settings and enemy point values
        """
        self.ship_speed *= self.speed_scale
        self.laser_speed *= self.speed_scale
        self.enemy_speed *= self.speed_scale    
        
        self.enemy_points = int(self.enemy_points * self.score_scale)  
         