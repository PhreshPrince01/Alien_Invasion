"""
MUSIC CREDIT

Credit
Distant Sky by Keys of Moon |
https://soundcloud.com/keysofmoon

Music promoted by 
https://www.chosic.com/free-music/all/

Creative Commons CC BY 4.0
https://creativecommons.org/licenses/by/4.0/
"""

import pygame
from pygame.sprite import Group
from alien_functions import create_fleet
from events import check_events
from game_functions import draw_pause_screen, update_screen
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from update_functions import update_aliens, update_bullets


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Load gun sound
    gun_sound = pygame.mixer.Sound("sounds\gun_sound.wav")

    # Make the play button.
    play_button = Button(screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    create_fleet(ai_settings, screen, ship, aliens)

    # Load and play in-game music
    try:
        pygame.mixer.music.load("sounds/Distant-Sky-Epic-Hybrid-Music-chosic.com_.wav")
        pygame.mixer.music.play(-1)  # Play the music in a loop
    except pygame.error as e:
        print(f"Error loading or playing music: {e}")

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, gun_sound)

        if stats.game_active:
            if stats.paused:
                draw_pause_screen(ai_settings, screen)
            else:
                ship.update()
                update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
                update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        else:
            update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()