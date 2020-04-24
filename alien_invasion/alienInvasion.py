# creating a pygame window and responding to user input

import sys # in order to exit the game when the player quits.

import pygame # contains the functions needed to make a game.

from settings import Settings # contains custom game settings

from ship import Ship # contains the ship

def runGame():
    # Initialize pygame, settings and screen object.
    pygame.init() # initializes background settings for pygame.
    
    ai_settings = Settings() # setting a display window.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)

    bg_color = (230, 230, 230) # set background color.

    # Start the main loop for the game
    while True:

        # watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # fill the screen with the background color.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most rececntly drawn screen visible.
        pygame.display.flip() # make the most resently draw screen visible

runGame()