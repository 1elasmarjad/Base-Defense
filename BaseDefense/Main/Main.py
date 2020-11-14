"""
AUTHOR      :   Jad El Asmar
Project     :   Base Defense
Description :   Defend your home base from unwanted enemy boats, ships, warships and airplanes.
Version     :   v0.1
"""

from Weapons import Weapon, Projectile
from Player import Player
from Entites import Enemy, EnemyList
from UserInterface import Text
from Debug import Point_Finder
import pygame

# CONSTANTS
DEFAULT_SCREEN_WIDTH = 1900
DEFAULT_SCREEN_HEIGHT = 1000

OCEAN_BLUE = (73, 136, 248)

DEFAULT_WEAPON = Weapon.WaterGun(40)

pygame.init()
pygame.display.set_caption("Base Defense")
running = True

display = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pygame.SCALED and pygame.RESIZABLE)
pygame.mouse.set_visible(False)
font = pygame.font.Font(pygame.font.get_default_font(), 24)
clock = pygame.time.Clock()

FRAME_RATE = 100

last_shot = pygame.time.get_ticks()

"""
----------------------------------
         ↓ GAME METHODS ↓
----------------------------------
"""


def cursor_app(display):
    x, y = pygame.mouse.get_pos()  # get mouse positions
    scope = pygame.image.load('scope.png').convert_alpha()
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

en = Enemy.SmallWoodenBoat(200, 200)

while running:
    # ---------------------INIT--------------------
    display.fill(OCEAN_BLUE)  # background colour

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # not hovering over shop

            x, y = pygame.mouse.get_pos()  # get mouse positions
            current_shot = pygame.time.get_ticks()
            time_dif = current_shot - last_shot

            if time_dif > player.inventory.current_weapon.rate_of_fire * 100:
                last_shot = current_shot
                player.shoot(x, y, display, font)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player.inventory.equip_next_weapon()
                print(player.inventory.current_weapon)

    # ---------------------INIT--------------------

    EnemyList.EnemyList.draw_all(display, False)  # draws all enemies
    check_essentials(display)  # checks essentials such as movement

    # current_weapon_text = font.render(str(player.inventory.current_weapon), False, (0, 0, 0))
    # display.blit(current_weapon_text, (pygame.display.get_window_size()[0]/2 - 100, 0))

    Text.DamageText.draw_all(display, font)  # displays all damage text on the screen
    Projectile.ProjectileList.draw_all(display)
    # check_inessentials(display)

    # ---------------------UPDATE------------------
    pygame.display.update()  # update display
    clock.tick(FRAME_RATE)
    # ---------------------UPDATE------------------
