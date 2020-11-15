"""
AUTHOR      :   Jad El Asmar
Project     :   Base Defense
Description :   Defend your home base from unwanted enemy boats, ships, warships and airplanes.
Version     :   v0.1
"""

from Weapons import Weapon, Projectile
from Player import Player
from Entites import Enemy, EnemyList, Round
from UserInterface import Text
import pygame
from Debug import Point_Finder

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
    scope = pygame.image.load('scope.png')
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

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player.x <= pygame.display.get_window_size()[
        0] - 50 and player.x < 1160 - 32:
        player.move_right(clock.tick())

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and player.x >= 0 and player.x > 760:
        player.move_left(clock.tick())


"""
----------------------------------
          ↓ GAME LOOP ↓
----------------------------------
"""

player = Player.Player(DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2)

player.inventory.add_to_inventory(DEFAULT_WEAPON)  # give watergun as default weapon

while running:
    # ---------------------INIT--------------------
    display.fill(OCEAN_BLUE)  # background colour
    pygame.draw.rect(display, (200, 170, 60), (760, 0, 400, 1080))

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
            if event.key == pygame.K_SPACE and Round.Round.round_ended:
                Round.Round.next_round()
                Round.Round.start_round()

    # ---------------------INIT--------------------

    EnemyList.EnemyList.draw_all(display, False)  # draws all enemies

    check_essentials(display)  # checks essentials such as movement

    Text.DamageText.draw_all(display, font)  # displays all damage text on the screen
    Projectile.ProjectileList.draw_all(display)  # display projectiles

    Round.Round.check_round(EnemyList.EnemyList.count_enemies(), display)  # checks if round is done or not

    # ---------------------UPDATE------------------
    pygame.display.update()  # update display
    clock.tick(FRAME_RATE)
    # ---------------------UPDATE------------------
