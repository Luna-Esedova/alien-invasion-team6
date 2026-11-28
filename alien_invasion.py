import os
import sys
import pygame


from settings import Settings
from ship import Ship


def run_game() -> None:
    """Initialize the game, audio system, and start the main loop."""
    pygame.init()
    pygame.mixer.init()


    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)


    clock = pygame.time.Clock()
    ship = Ship(ai_settings, screen)

    # Load sound effect if avaliable in assets folder
    shoot_sound = None
    sound_path = os.path.join("assets", "shoot.wav")
    if os.path.exists(sound_path):
        shoot_sound = pygame.mixer.Sound(sound_path)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
        

        ship.update()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_game()
    


