import pygame
import os


class UI:

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    ammo_path = os.path.join(THIS_FOLDER, 'ammoUI.png')
    ammo_img = pygame.image.load(ammo_path)

    watergun_path = os.path.join(THIS_FOLDER, 'watergunUI.png')
    watergun_img = pygame.image.load(watergun_path)

    sniper_path = os.path.join(THIS_FOLDER, 'sniperUI.png')
    sniper_img = pygame.image.load(sniper_path)

    @classmethod
    def healthbar(cls, canvas, bar_x, bar_y, bar_thickness, health, max_health, alive):
        if alive:
            pygame.draw.rect(canvas, (255, 0, 0), (bar_x, bar_y, max_health * 1.5, bar_thickness))
            pygame.draw.rect(canvas, (0, 255, 0), (bar_x, bar_y, health * 1.5, bar_thickness))
        else:
            pygame.draw.rect(canvas, (255, 0, 0), (bar_x, bar_y, max_health * 1.5, bar_thickness))

    @classmethod
    def weapon(cls, canvas, weapon, alive):
        ammo_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        if alive:
            # AMMO:
            ammo_text = ammo_font.render(f"{weapon.ammo}/{weapon.ammo_cap}", False, (0, 0, 0))
            ammo_text_rect = ammo_text.get_rect(center=(960, 930))
            canvas.blit(ammo_text, ammo_text_rect)

            ammo_rect = cls.ammo_img.get_rect(center=(1045, 926))
            canvas.blit(cls.ammo_img, ammo_rect)
            # WEAPON:
            x, y = 870, 926
            if weapon.name == "Water Gun":
                weapon_rect = cls.watergun_img.get_rect(center=(x, y))
                canvas.blit(cls.watergun_img, weapon_rect)
            elif weapon.name == "Pistol":
                print("TODO")  # TODO
            elif weapon.name == "Sniper":
                weapon_rect = cls.sniper_img.get_rect(center=(x, y))
                canvas.blit(cls.sniper_img, weapon_rect)
