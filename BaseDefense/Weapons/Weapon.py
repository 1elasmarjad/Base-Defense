"""
WEAPONS

damage = the damage a weapon does (optimally)
range = the range of the weapon until damage drops off
rate of fire = the speed in which a given weapon can attack
ammo cap = the capacity of how much ammo a given weapon can hold
ammo = the ammo a given weapon has

#todo
    - add a reload
    - add more weapons
"""

import math
import random


class Weapon:
    def __init__(self, name, damage, rate_of_fire, ammo_cap, weapon_range, ammo):
        self.name = name
        self.damage = damage
        self.weapon_range = weapon_range
        self.rate_of_fire = rate_of_fire
        self.ammo_cap = ammo_cap
        self.ammo = ammo

    def reload(self):
        print("TODO")  # TODO

    def fire(self, xFrom, yFrom, xTo, yTo, canvas):
        xFrom += 25  # changes from location to accurate location
        yFrom += 25

        # if xTo

        print(self.damage_done(xFrom, yFrom, xTo, yTo))

    def damage_done(self, xFrom, yFrom, xTo, yTo):
        if self.distance(xFrom, yFrom, xTo, yTo) >= self.weapon_range:  # out of range:
            return self.__random_damage(self.damage, 5, 2)
        else:  # in range:
            return self.__random_damage(self.damage, 2, 1)

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

    def __random_damage(self, dmg, consistency1, consistency2):
        return random.randint(dmg / consistency1, dmg / consistency2)

    def __str__(self):
        return f"{self.name}"


class WaterGun(Weapon):
    pass
    __NAME = "Water Gun"
    __DAMAGE = 40
    __RANGE_OF_FIRE = 300
    __RATE_OF_FIRE = 5
    __AMMO_CAP = 140

    def __init__(self, ammo_given):
        super().__init__(self.__NAME, self.__DAMAGE, self.__RATE_OF_FIRE,
                         self.__AMMO_CAP, self.__RANGE_OF_FIRE, ammo_given)


class Sniper(Weapon):
    pass
    __NAME = "Sniper"
    __DAMAGE = 60
    __RANGE_OF_FIRE = 1200
    __RATE_OF_FIRE = 1
    __AMMO_CAP = 60

    def __init__(self, ammo_given):
        super().__init__(self.__NAME, self.__DAMAGE, self.__RATE_OF_FIRE,
                         self.__AMMO_CAP, self.__RANGE_OF_FIRE, ammo_given)
