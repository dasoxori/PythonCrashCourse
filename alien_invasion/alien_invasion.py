# creating an empty Pygame window

import pygame # module that contains the functionality to make the game.

from settings import Settings # settings module

from ship import Ship # module ship

import gameFunctions as gf # function module

def runGame():
    # Initialize game and create a screen object.
    pygame.init() # initialize background settings
    aiSettings = Settings()
    screen = pygame.display.set_mode(
        (aiSettings.screen_width, aiSettings.screen_height))

    pygame.display.set_caption("Alien Invasion") # give a name to the head screen

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.checkEvents(ship)
        ship.update()
        gf.updateScreen(aiSettings, screen, ship)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


runGame()