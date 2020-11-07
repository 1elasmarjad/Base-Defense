class Inventory:

    def __init__(self, invSize):
        if invSize < 1:
            invSize = 1
        self.inventory_size = invSize # int
        self.items = 0 # int
        self.inv = []

    def add_to_inventory(self, weapon):
        if self.items >= self.size():
            print(f"Could not add to inventory - FULL - {self.items}/{self.inventory_size}")
            return False
        else:
            print(f"Added to inventory - {self.items}/{self.inventory_size}")
            self.inv.append(weapon)
            return True

    def size(self):
        counter = 0
        for x in self.inv:
            counter += 1
        return counter




