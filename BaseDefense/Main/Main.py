"""
AUTHOR      :   Jad El Asmar
Project     :   Base Defense
Description :   Defend your home base from unwanted enemy boats, ships, warships and airplanes.
Version     :   v0.1
"""

from Weapons import Weapon
from Player import Player
import pygame

# CONSTANTS
DEFAULT_SCREEN_WIDTH = 1900
DEFAULT_SCREEN_HEIGHT = 1000

OCEAN_BLUE = (73, 136, 248)

DEFAULT_WEAPON = Weapon.WaterGun(50)
TEST_WEAPON = Weapon.Sniper(20)

pygame.init()
pygame.display.set_caption("Base Defense")
running = True

display = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pygame.SCALED and pygame.RESIZABLE)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

"""
----------------------------------
         ↓ GAME METHODS ↓
----------------------------------
"""


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def cursor_app(display):
    x, y = pygame.mouse.get_pos()  # get mouse positions
    scope = pygame.image.load(r'C:/Users/Jad/Desktop/Base-Defense/BaseDefense/Player/scope.png').convert_alpha()
    display.blit(scope, (x, y))  # displays scope
    player.shoot(x, y, display)  # checks if player has shot


def check_movement():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w] and player.y >= 0:
        player.move_up(clock.tick())

    if keys[pygame.K_DOWN] or keys[pygame.K_s] and player.y <= pygame.display.get_window_size()[1] - 50:
        player.move_down(clock.tick())

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player.x <= pygame.display.get_window_size()[0] - 50:
        player.move_right(clock.tick())

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and player.x >= 0:
        player.move_left(clock.tick())

    player.draw(display)  # draw player


def check_essentials(display):
    check_movement()
    player.draw(display)
    cursor_app(display)


# def check_inessentials(display):
#     print("TODO")  # TODO


"""
----------------------------------
          ↓ GAME LOOP ↓
----------------------------------
"""

player = Player.Player(DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2)

player.inventory.add_to_inventory(DEFAULT_WEAPON)  # give watergun as default weapon

while running:
    # ---------------------INIT--------------------
    check_events()  # checks events, such as mouse clicked and tab closed
    display.fill(OCEAN_BLUE)  # background colour
    # ---------------------INIT--------------------

    check_essentials(display)
    # check_inessentials(display)

    # ---------------------UPDATE------------------
    pygame.display.update()  # update display
    clock.tick(100)
    # ---------------------UPDATE------------------
