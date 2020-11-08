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

DEFAULT_WEAPON = Weapon.WaterGun(50)

OCEAN_BLUE = (73, 136, 248)

pygame.init()
pygame.display.set_caption("Base Defense")
running = True

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


def cursor_app(x, y, display):
    scope = pygame.image.load(r'C:/Users/Jad/Desktop/Base-Defense/BaseDefense/Player/scope.png').convert_alpha()
    display.blit(scope, (x, y))


def check_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move_up()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move_right()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move_down()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move_left()

    if keys[pygame.K_e]:
        player.open_inventory()

    # if keys[pygame.K_f] && close_to_shop:
    #     #  TODO

    player.draw(display)  # draw
    pygame.display.update()  # update display


"""
----------------------------------
          ↓ GAME LOOP ↓
----------------------------------
"""
display = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pygame.SCALED and pygame.RESIZABLE)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

player = Player.Player(DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2)
player.inventory.add_to_inventory(DEFAULT_WEAPON)  # give watergun as default weapon
while running:
    # ---------------------INIT--------------------
    check_events()  # checks events, such as mouse clicked and tab closed
    display.fill(OCEAN_BLUE)  # background colour
    check_input()  # checks for input
    # ---------------------INIT--------------------

    player.draw(display)
    mouse_x, mouse_y = pygame.mouse.get_pos()  # get mouse positions
    cursor_app(mouse_x, mouse_y, display)  # adds graphics to the cursor

    # ---------------------UPDATE------------------
    pygame.display.update()  # update display
    clock.tick(60)
    # ---------------------UPDATE------------------
