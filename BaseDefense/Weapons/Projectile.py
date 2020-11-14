import math
import pygame


class ProjectileList:
    bullets = []

    @classmethod
    def draw_all(cls, canvas):
        try:
            for i in range(len(cls.bullets)):
                cls.bullets[i].draw(canvas)
        except IndexError:
            print("[BUG] bullets shot too fast; no impact on gameplay")

    @classmethod
    def add(cls, new):
        cls.bullets.append(new)

    @classmethod
    def add(cls, start_x, start_y, end_x, end_y, speed, r, g, b):
        obj = Projectile(start_x, start_y, end_x, end_y, speed, r, g, b)
        cls.bullets.append(obj)

    @classmethod
    def remove_projectile(cls, rmv):
        cls.bullets.remove(rmv)

    @classmethod
    def remove_projectile_index(cls, index):
        cls.bullets.pop(index)


class Projectile:

    def __init__(self, start_x, start_y, end_x, end_y, speed, r, g, b):
        self.x = start_x + 16
        self.y = start_y + 16
        self.end_x = end_x + 16
        self.end_y = end_y + 16
        self.speed = speed
        self.r = r
        self.g = g
        self.b = b




    def draw(self, canvas):



        print(self.x, self.y)

        # DRAW :
        pygame.draw.rect(canvas, (self.r, self.g, self.b), (self.x, self.y, 5, 5))
