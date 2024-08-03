import pygame
from bullet import Bullet
from alien_functions import create_fleet

"""
This module will handle the main game functions
"""

def toggle_pause(stats):
    """Toggle the pause state"""
    if stats.game_active:
        stats.paused = not stats.paused


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks 'Play'."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stat()
        stats.game_active = True
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Draw the score information.
    sb.show_score()
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    # Display the pause message.
    display_pause_message(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def display_pause_message(screen):
    """Display the pause message on the screen."""
    font = pygame.font.SysFont(None, 24)
    pause_message = font.render("Press 'P' to Pause", True, (255, 255, 255))
    screen_rect = screen.get_rect()
    pause_rect = pause_message.get_rect()
    pause_rect.topright = screen_rect.topright
    screen.blit(pause_message, pause_rect)


def draw_pause_screen(ai_settings, screen):
    """Draw the pause screen"""
    screen.fill(ai_settings.bg_color)
    font = pygame.font.SysFont(None, 48)
    pause_text = font.render("Paused. Press 'P' to Resume", True, (255, 0, 0))
    text_rect = pause_text.get_rect()
    text_rect.center = screen.get_rect().center
    screen.blit(pause_text, text_rect)
    pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets, gun_sound):
    """Fire a bullet if limit not reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        gun_sound.play()
