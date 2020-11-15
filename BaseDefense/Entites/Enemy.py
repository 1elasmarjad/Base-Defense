"""
ENEMIES

health: amount of health a given entity has before it dies.
rng: the range/ how far a entity can be to deal damage.
damage: the damage an entity will generally do when attacking.
speed: the speed/ how fast the entity moves.

"""

import pygame
from Entites import EnemyList
from Debug import Point_Finder


class Enemy:

    def __init__(self, x, y, name, health, attack_damage, speed, rng, stop_distance):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.speed = speed
        self.rng = rng
        self.stop_distance = stop_distance
        EnemyList.EnemyList.add(self)

        if self.x > 1128:
            self.left_sided = False
        elif self.x < 728:
            self.left_sided = True

    @property
    def loc(self):
        return self.x, self.y

    @loc.setter
    def loc(self, x, y):
        self.x = x
        self.y = y

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def attack_damage(self):
        return self.__attack_damage

    @attack_damage.setter
    def attack_damage(self, attack_damage):
        self.__attack_damage = attack_damage

    @property
    def rng(self):
        return self.__rng

    @rng.setter
    def rng(self, rng):
        self.__rng = rng

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def dead(self):
        if self.__health <= 0:
            return True
        return False

    def kill_self(self):
        EnemyList.EnemyList.remove(self)
        del self

    def __str__(self):
        return f"{self.name} | {self.enemiesCounter} | {self.x},{self.y} | {self.health}"


class SmallWoodenBoat(Enemy):
    pass
    __HEALTH = 40
    __ATTACK_DAMAGE = 10
    __RNG = 5
    __SPEED = 3
    __STOP_DISTANCE = 200
    __NAME = "Small Wooden Boat"

    def __init__(self, x, y):
        super().__init__(x, y, self.__NAME, self.__HEALTH, self.__ATTACK_DAMAGE, self.__SPEED,
                         self.__RNG, self.__STOP_DISTANCE)
        self.points = ([self.x, self.y], [self.x + 32, self.y], [self.x + 32, self.y + 32], [self.x, self.y + 32])

    def draw(self, canvas):
        if not self.dead:  # not dead:
            if self.left_sided and self.x <= 728 - self.__STOP_DISTANCE:
                self.x += self.__SPEED
            elif not self.left_sided and self.x >= 1128 + self.__STOP_DISTANCE:
                self.x -= self.__SPEED

            self.update_hit_box()
            pygame.draw.rect(canvas, (0, 0, 255), (self.x, self.y, 32, 32))  # TODO
        else:  # is dead:
            self.kill_self()

    def draw_hitbox(self, canvas):
        self.update_hit_box()
        Point_Finder.Point_Finder.point(canvas, self.points[0][0], self.points[0][1])
        Point_Finder.Point_Finder.point(canvas, self.points[1][0], self.points[1][1])
        Point_Finder.Point_Finder.point(canvas, self.points[2][0], self.points[2][1])
        Point_Finder.Point_Finder.point(canvas, self.points[3][0], self.points[3][1])

    def update_hit_box(self):
        self.points = ([self.x, self.y], [self.x + 32, self.y], [self.x + 32, self.y + 32], [self.x, self.y + 32])

    def get_hit_point(self, point):
        if point == 1:
            return self.points[0][0], self.points[0][1]
        elif point == 2:
            return self.points[1][0], self.points[1][1]
        elif point == 3:
            return self.points[2][0], self.points[2][1]
        elif point == 4:
            return self.points[3][0], self.points[3][1]
