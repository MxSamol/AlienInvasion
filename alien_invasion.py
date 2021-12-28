import pygame

from settings import Settings
import game_functions
from ship import Ship
from pygame.sprite import Group
from button import Button
from game_stats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    icon = pygame.image.load('images/icon.bmp')
    pygame.display.set_icon(icon)
    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)

    while True:
        game_functions.check_events(ai_settings, screen, ship, aliens, bullets, play_button, stats)
        ship.update()
        game_functions.update_bullets(ai_settings, screen, ship, aliens, bullets, stats)
        game_functions.update_aliens(ai_settings, screen, ship, aliens, bullets, stats)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats)

run_game()