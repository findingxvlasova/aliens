import sys
from ship import Ship
from settings import Settings
import gameFunctions as gf
import pygame
from pygame.sprite import Group

def runGame():
    pygame.init() 
    aiSettings = Settings() 
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight)) 
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(aiSettings, screen)
    bullets = Group()


    while True: #главный цикл игры
        gf.checkEvents(aiSettings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateScreen(aiSettings, screen, ship, bullets)


runGame()
