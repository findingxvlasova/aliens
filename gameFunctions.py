import sys
import pygame
from bullet import Bullet


def checkKeydownEvents(event, aiSettings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingleft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings, screen, ship, bullets)


def checkKeyupEvents(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingleft = False


def checkEvents(aiSettings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, aiSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)

def updateScreen(aiSettings, screen, ship, bullets):
    screen.fill(aiSettings.bgColor)
    for bullet in bullets.sprites():
        bullet.drawBullet()

    ship.blitme()
    pygame.display.flip()


def updateBullets(bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fireBullet(aiSettings, screen, ship, bullets  ):
    if len(bullets) <= aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)
