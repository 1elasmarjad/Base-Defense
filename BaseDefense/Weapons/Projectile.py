import math
import pygame

class ProjectileList:
    bullets = []

    @classmethod
    def draw_all(cls, canvas):
        for i in range(len(cls.bullets)):
            cls.bullets[i].draw(canvas)

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
        self.start_x = start_x + 16
        self.start_y = start_y + 16
        self.end_x = end_x + 16
        self.end_y = end_y + 16
        self.speed = speed
        self.colour = r, g, b

    def draw(self, canvas):
        # calculations:
        if self.start_x != self.end_x and self.start_y != self.end_y:
            pygame.draw.rect(canvas, (self.r,self.g,self.b), self.start_x, self.start_y )
            slope_x = (self.end_x - self.start_x)
            slope_y = (self.end_y - self.start_y)
            ang = math.atan2(slope_y, slope_x)
            self.start_x += math.cos(ang) * self.vel
            self.start_y += math.sin(ang) * self.vel

