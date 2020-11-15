import pygame
import os


class UI:
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(THIS_FOLDER, 'ammoUI.png')
    ammo_img = pygame.image.load(path)

    @classmethod
    def healthbar(cls, canvas, bar_x, bar_y, bar_thickness, health, max_health, alive):
        if alive:
            pygame.draw.rect(canvas, (255, 0, 0), (bar_x, bar_y, max_health * 1.5, bar_thickness))
            pygame.draw.rect(canvas, (0, 255, 0), (bar_x, bar_y, health * 1.5, bar_thickness))
        else:
            pygame.draw.rect(canvas, (255, 0, 0), (bar_x, bar_y, max_health * 1.5, bar_thickness))

    @classmethod
    def ammo(cls, canvas, x, y, weapon, alive):
        ammo_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        if alive:
            ammo_text = ammo_font.render(f"{weapon.ammo}/{weapon.ammo_cap}", False, (0, 0, 0))
            ammo_text_rect = ammo_text.get_rect(center=(960, 930))
            canvas.blit(ammo_text, ammo_text_rect)

            ammo_rect = cls.ammo_img.get_rect(center=(1045, 926))
            canvas.blit(cls.ammo_img, ammo_rect)
