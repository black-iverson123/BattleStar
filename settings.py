class Settings:
    """_summary_: A class to keep game settings
    """
    
    def __init__(self):
        """_summary_: game settings initialized
        """
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        
        #ship settings
        self.ship_speed = 1.5
        
        #laser settings
        self.laser_speed = 1.0
        self.laser_width = 3
        self.laser_height = 15
        self.laser_colour = (255, 0, 0)
        self.allowed_lasers = 5