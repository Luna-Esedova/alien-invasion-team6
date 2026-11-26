import pygame


class Ship:
    """Oyunçunun kosmik gəmisini və hərəkət məntiqini təmsil edən sinif."""

    def __init__(self, ai_settings, screen):
        """Gəmini qurur və ekranın alt mərkəzinə yerləşdirir."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Gəmi təsvirini yükləyir, ölçüləndirir və rect obyektini alır
        self.image = pygame.image.load("assets/ship.png")
        self.image = pygame.transform.scale(self.image, (80, 60))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Gəmini ekranın alt mərkəzinə yerləşdirir
        self.rect.midbottom = self.screen_rect.midbottom

        # Kəsr dəqiqliklə (float) üfüqi mərkəz koordinatı
        self.center = float(self.rect.centerx)

        # Hərəkət bayraqları
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Hərəkət bayraqları və ekran sərhədlərinə görə gəminin yerini yeniləyir."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Gəmini cari mövqeyində ekranda çəkir."""
        self.screen.blit(self.image, self.rect)


if __name__ == "__main__":
    # Rol 2-ni digər modullar olmadan təkbaşına yoxlamaq üçün kiçik sınaq
    class DummySettings:
        """Sınaq üçün müvəqqəti parametrlər sinfi."""

        def __init__(self):
            self.screen_width = 800
            self.screen_height = 600
            self.bg_color = (20, 24, 40)
            self.ship_speed_factor = 3.0

    pygame.init()
    test_settings = DummySettings()
    test_screen = pygame.display.set_mode(
        (test_settings.screen_width, test_settings.screen_height)
    )
    pygame.display.set_caption("Ship Test")

    ship = Ship(test_settings, test_screen)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_q:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        ship.update()
        test_screen.fill(test_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
