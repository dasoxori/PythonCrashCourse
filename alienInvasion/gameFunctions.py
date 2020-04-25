import sys
import pygame

def checkKeydownEvents(event, ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
            
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True

def checkKeyupEvents(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False

    

def checkEvents(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, ship)
           
            
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)
            


def updateScreen(aiSettings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(aiSettings.bgColor)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()