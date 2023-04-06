import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')  # load image of ship
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)                       # float value for ship with speed 1.5)

        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False  # motion indicator
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ update new position of ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed     # update  ship.x instead rect
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x                        # update rect with self.x
