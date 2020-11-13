import pygame


class Point_Finder:

    @classmethod
    def point(cls, display, x, y):
        pygame.draw.rect(display, (0, 255, 0), (x, y, 3, 3))
