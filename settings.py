class Settings:
    """Store configuration values for the game."""
    def __init__(self) -> None:
         """Initialize game settings."""
          # Window and background theme settings
          self.screen_width = 1200
          self.screen_height = 800
          self.bg_color = (18, 24, 38)
          self.caption = "Cyber Defence - Alien Invasion"
          
          
          # Player ship movement settings
          self.ship_speed_factor = 1.5
          
          # Projectile settings
          self.bullet_speed_factor = 2.5
          self.bullet_width = 4
          self.bullet_height = 16
          self.bullet_color = (80, 220, 255)
          self.bullets_allowed = 3






