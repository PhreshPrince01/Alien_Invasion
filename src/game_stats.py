class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stat()

        #Start game in an inactive state
        self.game_active = False
        self.paused = False

        # High score should nevr be reset
        self.high_score = 0

    def reset_stat(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1