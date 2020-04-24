# Creating a Settings Class

class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializze the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bgColor = (230, 230, 230)