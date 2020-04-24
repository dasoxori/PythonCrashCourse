# collect game functions
# check_events()

import sys

import pygame

def checkEvents(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def updateScreen(aiSettings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(aiSettings.bgColor)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()