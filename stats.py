class Stats:
    """_summary_: Track stats for game
    """
    
    def __init__(self, ai_game):
        """_summary_: Initialize stats
        """
        self.settings = ai_game.settings
        self.reset_stats()
        
        #starting alien invasion in active state
        self.game_active = False
        
        #Highest scores should be made permanent
        self.best_score = 0
    
    def reset_stats(self):
        """_summary_: Initialize stats that change during gameplay
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1