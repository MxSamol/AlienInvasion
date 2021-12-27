import pygame
from settings import Settings


class Ship():
    def __init__(self, ai_screen):
        self.screen = ai_screen
        self.settings = Settings()
        self.screen_rect = ai_screen.get_rect()
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def bltime(self):
        self.screen.blit(self.image, self.rect)