"""
AUTHOR      :   Jad El Asmar
Project     :   Base Defense
Description :   Defend your home base from unwanted enemy boats, ships, warships and airplanes.
Version     :   v0.1
"""

from Player import Player
import pygame

# CONSTANTS
DEFAULT_SCREEN_WIDTH = 1900
DEFAULT_SCREEN_HEIGHT = 1000

OCEAN_BLUE = (73, 136, 248)

pygame.init()
pygame.display.set_caption("Base Defense")
running = True

"""
----------------------------------
         ↓ GAME METHODS ↓
----------------------------------
"""


def checkForClose():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def checkMovement():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move_up()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move_right()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move_down()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move_left()

    player.draw(gameDisplay)  # draw
    pygame.display.update()  # update display


"""
----------------------------------
          ↓ GAME LOOP ↓
----------------------------------
"""
gameDisplay = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pygame.SCALED and pygame.RESIZABLE)
player = Player.Player(DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2)
while running:
    # ---------------------INIT--------------------
    pygame.time.delay(30)
    checkForClose()  # checks if the game has been closed
    checkMovement()  # checks if any movement keys were pressed
    gameDisplay.fill(OCEAN_BLUE)  # background colour

    # ---------------------INIT--------------------

    player.draw(gameDisplay)
    pygame.display.update()  # update display
