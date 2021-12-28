import pygame

from settings import Settings
import game_functions
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    icon = pygame.image.load('images/icon.bmp')
    pygame.display.set_icon(icon)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        game_functions.check_events(ai_settings, screen, ship, aliens, bullets)
        ship.update()
        game_functions.update_bullets(ai_settings, screen, ship, aliens, bullets)
        game_functions.update_aliens(ai_settings, screen, ship, aliens, bullets)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()