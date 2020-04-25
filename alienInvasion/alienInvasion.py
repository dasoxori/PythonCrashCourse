import pygame
from settings import Settings
from ship import Ship
import gameFunctions as gf 

def runGame():

    # Initialize game and create a screen object.
    pygame.init() # initialize background settings
    pygame.display.set_caption("Alien Invasion")

    # Set background size.
    aiSettings = Settings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHeight))
    
    # Make a ship.
    ship = Ship(aiSettings, screen)

    # Start main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.checkEvents(ship)
        ship.update()
        gf.updateScreen(aiSettings, screen, ship)

runGame()