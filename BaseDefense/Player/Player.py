from Player import Inventory
import pygame


class Player:
    _DEFAULT_COINS = 1000
    _DEFAULT_INVENTORY_SIZE = 2
    _DEFAULT_HEALTH = 130
    _DEFAULT_ARMOR = 20
    _HEAL_DELAY = 50

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._coins = Player._DEFAULT_COINS
        self._alive = True
        self.inventory = Inventory.Inventory(Player._DEFAULT_INVENTORY_SIZE)
        self._health = Player._DEFAULT_HEALTH
        self._armor = Player._DEFAULT_ARMOR

    def has_enough(self, price):
        if self._coins >= price:
            return True
        else:
            return False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, coins):
        self._coins = coins

    def add_coins(self, added):
        self._coins += added

    def remove_coins(self, removed):
        self._coins = removed

    @property
    def alive(self):
        if self._health <= 0:
            return True
        else:
            return False

    def hurt(self, damage_done):
        self._health -= damage_done
        return self.alive()  # checks if player is still alive after damage is done

    def heal(self, healing_done):
        while self._health != self._DEFAULT_HEALTH:
            pygame.time.delay(self._HEAL_DELAY)
            self._health += 1

    def teleport(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        print("TODO")  # TODO
