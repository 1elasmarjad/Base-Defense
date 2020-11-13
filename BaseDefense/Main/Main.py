"""
AUTHOR      :   Jad El Asmar
Project     :   Base Defense
Description :   Defend your home base from unwanted enemy boats, ships, warships and airplanes.
Version     :   v0.1
"""

from Weapons import Weapon
from Player import Player
from Entites import Enemy, EnemyList
from Debug import Point_Finder
import pygame

# CONSTANTS
DEFAULT_SCREEN_WIDTH = 1900
DEFAULT_SCREEN_HEIGHT = 1000

OCEAN_BLUE = (73, 136, 248)

DEFAULT_WEAPON = Weapon.WaterGun(40)
TEST_WEAPON = Weapon.Sniper(15)

pygame.init()
pygame.display.set_caption("Base Defense")
running = True

display = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pygame.SCALED and pygame.RESIZABLE)
pygame.mouse.set_visible(False)
font = pygame.font.Font(pygame.font.get_default_font(), 42)
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  # get mouse positions
            player.shoot(x, y, display, font)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player.inventory.equip_next_weapon()
                print(player.inventory.current_weapon)


def cursor_app(display):
    x, y = pygame.mouse.get_pos()  # get mouse positions
    scope = pygame.image.load(r'C:/Users/Jad/Desktop/Base-Defense/BaseDefense/Player/scope.png').convert_alpha()
    display.blit(scope, (x, y))  # displays scope


def check_essentials(display):
    check_movement()
    player.draw(display)
    cursor_app(display)


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


# def check_inessentials(display):
#     if keys[pygame.K_r]:
#         print("TRUE")


"""
----------------------------------
          ↓ GAME LOOP ↓
----------------------------------
"""

player = Player.Player(DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2)

player.inventory.add_to_inventory(DEFAULT_WEAPON)  # give watergun as default weapon
player.inventory.add_to_inventory(TEST_WEAPON)

en = Enemy.SmallWoodenBoat(200, 200)

while running:
    # ---------------------INIT--------------------
    display.fill(OCEAN_BLUE)  # background colour
    check_events()  # checks events, such as mouse clicked and tab closed
    # ---------------------INIT--------------------

    EnemyList.EnemyList.draw_all(display, False)  # draws all enemies
    check_essentials(display)  # checks essentials such as movement

    current_weapon_text = font.render(str(player.inventory.current_weapon), False, (0, 0, 0))
    display.blit(current_weapon_text, (pygame.display.get_window_size()[0]/2 - 100, 0))

    # check_inessentials(display)

    # ---------------------UPDATE------------------
    pygame.display.update()  # update display
    clock.tick(100)
    # ---------------------UPDATE------------------
