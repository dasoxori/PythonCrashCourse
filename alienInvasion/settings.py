class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screenWidth = 1200
        self.screenHeight = 700
        self.bgColor = (230, 230, 230)

        # Ship settings
        self.shipSpeedFactor = 1.5