"""
AUTHOR      :   Jad El Asmar
Project     :   Base Defense
Description :   Defend your home base from unwanted enemy boats, ships, warships and airplanes.
Version     :   v0.1
"""

from Weapons import Weapon, Projectile
from Player import Player
from Entites import Enemy, EnemyList, Round
from UserInterface import DamageText, CoinText
import pygame
from Debug import Point_Finder

def main():

    # CONSTANTS
    DEFAULT_SCREEN_WIDTH = 1900
    DEFAULT_SCREEN_HEIGHT = 1000

    BULLET_PRICE = 1.5

    OCEAN_BLUE = (73, 136, 248)

    DEFAULT_WEAPON = Weapon.WaterGun(200)

    pygame.init()
    pygame.display.set_caption("Base Defense")
    running = True

    display = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pygame.SCALED and pygame.RESIZABLE)
    pygame.mouse.set_visible(False)
    font = pygame.font.Font(pygame.font.get_default_font(), 150)
    fade_font = pygame.font.Font(pygame.font.get_default_font(), 28)
    clock = pygame.time.Clock()

    FRAME_RATE = 100
    game_end = False

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
        if not game_end:

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

    player.inventory.add_to_inventory(DEFAULT_WEAPON)  # give water gun as default weapon

    while running:
        # ---------------------INIT--------------------
        display.fill(OCEAN_BLUE)  # background colour
        pygame.draw.rect(display, (200, 170, 60), (760, 0, 400, 1080))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_end and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()  # get mouse positions
                current_shot = pygame.time.get_ticks()
                time_dif = current_shot - last_shot

                if time_dif > player.inventory.current_weapon.rate_of_fire * 100:
                    last_shot = current_shot
                    player.shoot(x, y, display, fade_font, player)

            if event.type == pygame.KEYDOWN and not game_end:
                if event.key == pygame.K_r:
                    player.inventory.equip_next_weapon()
                    print(player.inventory.current_weapon)
                if event.key == pygame.K_SPACE and Round.Round.round_ended:
                    Round.Round.next_round()
                    Round.Round.start_round()
                if event.key == pygame.K_z and not game_end:
                    BULLET_PRICE = 2
                    bullets_needed = player.inventory.current_weapon.ammo_cap - player.inventory.current_weapon.ammo
                    ammo_price = bullets_needed * BULLET_PRICE

                    if player.coins >= ammo_price and player.inventory.current_weapon.ammo != player.inventory.current_weapon.ammo_cap:
                        player.inventory.current_weapon.ammo = player.inventory.current_weapon.ammo_cap
                        player.remove_coins(ammo_price)
                        CoinText.CoinText.add_less(display, ammo_price)

                    elif player.coins < ammo_price and player.inventory.current_weapon.ammo != player.inventory.current_weapon.ammo_cap:
                        temp_coins = player.coins
                        needed = 0
                        while temp_coins >= BULLET_PRICE:
                            needed += 1
                            temp_coins -= BULLET_PRICE

                        ammo_price = needed * BULLET_PRICE
                        player.inventory.current_weapon.ammo += needed
                        player.remove_coins(ammo_price)

                if event.key == pygame.K_e:
                    if player.inventory.open:
                        player.inventory.open = False
                    else:
                        player.inventory.open = True

        # ---------------------INIT--------------------

        EnemyList.EnemyList.draw_all(display, False, player, fade_font)  # draws all enemies

        check_essentials(display)  # checks essentials such as movement
        CoinText.CoinText.draw_all(display)

        DamageText.DamageText.draw_all(display, fade_font)  # displays all damage text on the screen
        Projectile.ProjectileList.draw_all(display)  # display projectiles

        Round.Round.check_round(EnemyList.EnemyList.count_enemies(), display)  # checks if round is done or not
        player.inventory.draw(display)

        if Round.Round.round_ended:
            player.heal_up()

        if not player.alive:
            end_text = font.render(f"Score: {Round.Round.rnd}", False, (250, 50, 0))
            end_text_rect = end_text.get_rect(center=(960, 510))
            display.blit(end_text, end_text_rect)

            end_text2 = font.render(f"You lost!", False, (250, 20, 0))
            end_text_rect.y -= 200
            display.blit(end_text2, end_text_rect)

            game_end = True

        # ---------------------UPDATE------------------
        pygame.display.update()  # update display
        clock.tick(FRAME_RATE)
        # ---------------------UPDATE------------------

