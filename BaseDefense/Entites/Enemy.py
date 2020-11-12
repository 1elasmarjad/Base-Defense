"""
ENEMIES

health: amount of health a given entity has before it dies.
rng: the range/ how far a entity can be to deal damage.
damage: the damage an entity will generally do when attacking.
speed: the speed/ how fast the entity moves.

"""

import pygame


class Enemy:
    enemiesCounter = 0  # counts the number of enemies there are

    def __init__(self, x, y, name, health, attack_damage, speed, rng):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.speed = speed
        self.rng = rng
        Enemy.enemiesCounter += 1

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
        print("TODO")
        # TODO

    def __str__(self):
        return f"{self.name} | {self.enemiesCounter} | {self.x},{self.y}"


class SmallWoodenBoat(Enemy):
    pass
    __HEALTH = 20
    __ATTACK_DAMAGE = 10
    __RNG = 5
    __SPEED = 20
    __NAME = "Small Wooden Boat"

    def __init__(self, x, y):
        super().__init__(x, y, self.__NAME, self.__HEALTH, self.__ATTACK_DAMAGE, self.__SPEED,
                         self.__RNG)
        self.points = ([self.x, self.y], [self.x + 64, self.y], [self.x + 64, self.y + 64], [self.x, self.y + 64])
        
    def draw(self, canvas):
        if not self.dead:
            pygame.draw.rect(canvas, (0, 0, 255), (self.x, self.y, 32, 32))  # TODO
        else:
            #is dead
            print("DEAD cannot draw")
