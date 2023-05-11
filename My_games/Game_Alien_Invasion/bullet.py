import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        # create object bullet on screen
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creat rect bullet in (0, 0) and set right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save position of bullet
        self.y = float(self.rect.y)


    def update(self):
        # move bullet up on screen
        self.y -= self.settings.bullet_speed
        # update position rect
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)