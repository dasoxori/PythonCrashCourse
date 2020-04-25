import pygame

class Ship():

    def __init__(self, aiSettings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen # is where we'll draw the ship.
        self.aiSettings = aiSettings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect() # we make the image have rectangles shape.
        self.screenRect = screen.get_rect() # we store the screen rect

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.movingRight = False
        self.movingLeft = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.center += self.aiSettings.shipSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.aiSettings.shipSpeedFactor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)