"""
WEAPONS

damage = the damage a weapon does (optimally)
damage drop off = the drop off to -damage per pixel
rate of fire = the speed in which a given weapon can attack
ammo cap = the capacity of how much ammo a given weapon can hold
ammo = the ammo a given weapon has

#todo
    - add a reload
    - add more weapons
"""

import pygame
import math


class Weapon:
    def __init__(self, name, damage, damage_drop_off, rate_of_fire, ammo_cap, ammo):
        self.name = name
        self.damage = damage
        self.damage_drop_off = damage_drop_off
        self.rate_of_fire = rate_of_fire
        self.ammo_cap = ammo_cap
        self.ammo = ammo

    def reload(self):
        print("TODO")  # TODO

    def fire(self, xFrom, yFrom, xTo, yTo, canvas):
        # DRAW BULLET
        xFrom += 25  # changes from location to accurate location
        yFrom += 25

        print(self.damage_done(xFrom, yFrom, xTo, yTo))

    def damage_done(self, xFrom, yFrom, xTo, yTo):
        # return self.damage - (self.distance(xFrom, yFrom, xTo, yTo) * self.damage_drop_off) TODO bullet drop off formula
        print("TODO")

    def distance(self, xFrom, yFrom, xTo, yTo):
        distance = math.sqrt(math.pow(xTo - xFrom, 2) + math.pow(yTo - yFrom, 2))
        if distance <= 0:
            distance = 1
        return distance

    def giveAmmo(self, amount):
        if self.ammo + amount > self.ammo_cap:
            return False  # could not give ammo
        else:
            self.ammo += amount
            return True  # able to give ammo

    def get_ammo(self):
        return self.ammo

    def get_ammo_cap(self):
        return self.ammo_cap

    def __str__(self):
        return f"{self.name}"


class WaterGun(Weapon):
    pass
    __NAME = "Water Gun"
    __DAMAGE = 50
    __DAMAGE_DROP_OFF = 0.5
    __RATE_OF_FIRE = 5
    __AMMO_CAP = 140

    def __init__(self, ammo_given):
        super().__init__(self.__NAME, self.__DAMAGE, self.__DAMAGE_DROP_OFF, self.__RATE_OF_FIRE,
                         self.__AMMO_CAP, ammo_given)


class Sniper(Weapon):
    pass
    __NAME = "Sniper"
    __DAMAGE = 90
    __DAMAGE_DROP_OFF = 0.001
    __RATE_OF_FIRE = 3
    __AMMO_CAP = 60

    def __init__(self, ammo_given):
        super().__init__(self.__NAME, self.__DAMAGE, self.__DAMAGE_DROP_OFF, self.__RATE_OF_FIRE,
                         self.__AMMO_CAP, ammo_given)
