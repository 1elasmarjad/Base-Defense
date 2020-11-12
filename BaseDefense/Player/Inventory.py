from Weapons import Weapon


class Inventory:

    def __init__(self, inventory_cap):
        if inventory_cap < 1:
            inventory_cap = 1
        self.inventory_cap = inventory_cap  # int
        self.inv = []
        self.hovering_index = 0  # hovering over index 0

    def next_weapon(self):
        if self.hovering_index + 1 < len(self.inv):
            return self.inv[self.hovering_index]  # normal case
        else:
            return self.inv[0]  # go back to start of array

    def next_index(self):
        if self.hovering_index + 1 < len(self.inv):
            return self.hovering_index + 1
        else:
            return 0

    def equip_next_weapon(self):
        self.hovering_index = self.next_index()

    @property
    def current_weapon(self):
        return self.inv[self.hovering_index]

    @current_weapon.setter
    def current_weapon(self, wpn):
        self.inv[self.hovering_index] = wpn

    def weapon_at_index(self, index, wpn):
        self.hovering_index = index
        self.inv[index] = wpn

    def add_to_inventory(self, weapon):
        if self.inventory_cap <= self.size() != 0:
            print(f"Could not add to inventory - FULL - {self.size()}/{self.inventory_cap}")
            return False
        else:
            self.inv.append(weapon)
            print(f"Added to inventory - {self.size()}/{self.inventory_cap}")
            return True

    def remove_index(self, index):
        if index > self.inventory_cap or index < 0:
            return False
        return self.inv.pop(index)

    def remove_weapon(self, weapon):
        counter = 0
        for i in self.inv:
            counter += 1
            if self.inv[counter - 1] == weapon:
                return self.remove_index(counter - 1)
        return False

    def get_current_weapon_ammo(self):
        current_weapon = self.current_weapon()
        return current_weapon.ammo, current_weapon.ammo_cap

    def size(self):
        counter = 0
        for x in self.inv:
            counter += 1
        return counter
