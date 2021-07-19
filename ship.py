import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images\ship.bmp')

        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        self.center = float(self.rect.centerx)

        #флаги перемещения
        self.movingRight = False
        self.movingleft = False

    def update(self):
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.center += self.ai_settings.shipSpeedFactor
        if self.movingleft and self.rect.left > 0:
            self.center -= self.ai_settings.shipSpeedFactor

        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)
