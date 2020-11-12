from Player import Inventory
import pygame


class Player:
    __DEFAULT_COINS = 1000
    __DEFAULT_INVENTORY_SIZE = 2
    __DEFAULT_HEALTH = 130
    __DEFAULT_ARMOR = 20
    __HEAL_DELAY = 50
    __MOVEMENT_FACTOR = 2

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__coins = Player.__DEFAULT_COINS
        self.__alive = True
        self.inventory = Inventory.Inventory(Player.__DEFAULT_INVENTORY_SIZE)
        self.__health = Player.__DEFAULT_HEALTH
        self.__armor = Player.__DEFAULT_ARMOR

    def move_up(self, dt):
        self.y -= self.__MOVEMENT_FACTOR
        return self.y

    def move_down(self, dt):
        self.y += self.__MOVEMENT_FACTOR
        return self.y

    def move_right(self, dt):
        self.x += self.__MOVEMENT_FACTOR
        return self.x

    def move_left(self, dt):
        self.x -= self.__MOVEMENT_FACTOR
        return self.x

    def has_enough(self, price):
        if self.__coins >= price:
            return True
        else:
            return False

    def shoot(self, shoot_to_x, shoot_to_y, canvas):
        if pygame.mouse.get_pressed()[0]:
            self.inventory.current_weapon.fire(self.x, self.y, shoot_to_x, shoot_to_y, canvas)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, coins):
        self.__coins = coins

    def add_coins(self, added):
        self.__coins += added

    def remove_coins(self, removed):
        self.__coins = removed

    @property
    def alive(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def hurt(self, damage_done):
        self.__health -= damage_done
        return self.alive()  # checks if player is still alive after damage is done

    def heal(self, healing_done):
        while self.__health != self.__DEFAULT_HEALTH:
            pygame.time.delay(self.__HEAL_DELAY)
            self.__health += 1

    # def open_inventory(self):
    #     dir()  TODO

    def teleport(self, x, y):
        self.__x = x
        self.__y = y

    def draw(self, canvas):
        pygame.draw.rect(canvas, (255, 0, 0), (self.x, self.y, 50, 50))  # TODO
