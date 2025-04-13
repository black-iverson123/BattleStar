import pygame.font

class Scoreboard:
    """_summary_: Class for game scores
    """
    
    def __init__(self, ai_game):
        """_summary_: initialize score keeping attribute
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        #font settings for scoring
        self.text_colour = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 20)
        
        # Prepare initial score image
        self.prep_score()
        self.prep_best_score()
        self.prep_level()
    
    def prep_score(self):
        """_summary_: score will be turned into a rendered image
        """
        round_score = round(self.stats.score, -1)
        score_str = f"Score: {round_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_colour,
                                            self.settings.bg_colour)
        #show score at top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_best_score(self):
        """_summary_: Highest score will be rendered in an image
        """
        best_score = round(self.stats.best_score, -1)
        best_score_str = f" Best Score: {best_score:,}"
        self.best_score_img = self.font.render(best_score_str, True, self.text_colour, self.settings.bg_colour)
        
        # Placing best score at top of the screen
        self.best_score_rect = self.best_score_img.get_rect()
        self.best_score_rect.centerx = self.screen_rect.centerx
        self.best_score_rect.top = self.score_rect.top
    
    def show_score(self):
        """_summary_:Draw score to the screen
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.best_score_img, self.best_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
    
    def check_best_score(self):
        """_summary_: checking for a new best score
        """
        if self.stats.score > self.stats.best_score:
            self.stats.best_score = self.stats.score
            self.prep_best_score()
    
    def prep_level(self):
        """_summary_: level will be displayed as an image
        """
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_colour, self.settings.bg_colour)
        
        # placing level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10