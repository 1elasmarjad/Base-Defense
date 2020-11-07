"""
AUTHOR      :   Jad El Asmar
Project     :   Base Defense
Description :   Defend your home base from unwanted enemy boats, ships, warships and airplanes.
"""

from Player import Inventory
from Player import Player
import pygame

# CONSTANTS
DEFAULT_SCREEN_WIDTH = 1200
DEFAULT_SCREEN_HEIGHT = 850

OCEAN_BLUE = (73, 136, 248)

# test = Enemy.Enemy(6, 4, "TEST", 20, 20, 20, 20)
#
# bbb = Enemy.SmallWoodenBoat(3, 3)
# print(Enemy.Enemy.enemiesCounter)

pygame.init()
pygame.display.set_caption("Base Defense")
running = True

test = Player.Player(5,5)




# def __checkForClose():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#
# gameDisplay = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), RESIZABLE)
# while running:
#     pygame.time.delay(100)
#     __checkForClose()
#
#     gameDisplay.fill((OCEAN_BLUE))
#
#     pygame.display.update()
