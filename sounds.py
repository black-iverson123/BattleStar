import pygame

class GameSounds:
    """_summary_: Class to manage game sounds."""

    def __init__(self, ai_game):
        """Initialize the game sounds."""
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
    
    def _play_back_sound(self, file_path, volume=0.2):
        """_summary_: Helper method to play background music
        """
        try:
            sound = pygame.mixer.Sound(file_path)
            sound.set_volume(volume)
            sound.play(-1)
        except pygame.error as e:
            print(f"Error playing background sound: {e}")

    def _play_sound(self, file_path, volume=0.2):
        """_summary_: Helper method to play a sound."""
        try:
            sound = pygame.mixer.Sound(file_path)
            sound.set_volume(volume)
            sound.play()
        except pygame.error as e:
            print(f"Error playing sound: {e}")

    def _play_laser_sound(self, color, volume=0.2):
        """_summary_: Helper function to play the laser sound based on the given laser color."""
        if color == (255, 0, 0):  # Red laser
            self._play_sound("assets/sounds/red_laser.wav", volume)
        elif color == (0, 0, 255):  # Blue laser
            self._play_sound("assets/sounds/blue_laser.wav", volume)
        elif color == (255, 165, 0):  # Orange laser
            self._play_sound("assets/sounds/orange_laser.wav", volume)

    def _contact_sound(self, volume=0.2):
        """_summary_: Helper function to play the sound when the ship is hit by an enemy."""
        self._play_sound("assets/sounds/explosion.aiff", volume)
    
    def _stop_sound(self):
        """_summary_: Helper function to stop sounds being played
        """
        pygame.mixer.stop()