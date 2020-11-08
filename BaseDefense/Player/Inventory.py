from Weapons import Weapon


class Inventory:

    def __init__(self, inventory_cap):
        if inventory_cap < 1:
            inventory_cap = 1
        self.inventory_cap = inventory_cap  # int
        self.inv = []
        self.hovering_index = 0  # hovering over index 0

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

    def next_weapon(self):
        self.hovering_index += 1 % self.inventory_cap

    def current_weapon(self):
        current_weapon = self.inv[self.hovering_index - 1]
        return current_weapon

    def get_current_weapon_ammo(self):
        current_weapon = self.inv[self.hovering_index - 1]
        print(current_weapon)
        print(getattr(current_weapon, 'get_ammo'))
        return getattr(current_weapon, 'get_ammo'.), getattr(current_weapon, 'get_ammo_cap') # todo



        # if hasattr(current_weapon, 'get_ammo') and callable(getattr(current_weapon, 'get_ammo')) \
        #         and hasattr(current_weapon, 'get_ammo_cap') and callable(getattr(current_weapon, 'get_ammo_cap')):
        #     return current_weapon.get_ammo, current_weapon.get_ammo_cap


        # object_methods = [method_name for method_name in dir(Weapon.Weapon)
        #                   if callable(getattr(Weapon.Weapon, method_name))]

    def size(self):
        counter = 0
        for x in self.inv:
            counter += 1
        return counter
