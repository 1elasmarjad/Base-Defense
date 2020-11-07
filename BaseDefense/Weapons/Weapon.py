class Weapon:
    def __init__(self, name, damage, damage_drop_off, reload_time, rate_of_fire, ammo_cap, ammo):
        self.name = name
        self.damage = damage
        self.damage_drop_off = damage_drop_off
        self.reload_time = reload_time
        self.rate_of_fire = rate_of_fire
        self.ammo_cap = ammo_cap
        self.ammo = ammo

    def reload(self):
        print("TODO")  # TODO

    def fire(self, x, y):
        print("TODO")  # TODO

    def giveAmmo(self, amount):
        if self.ammo + amount > self.ammo_cap:
            return False  # could not give ammo
        else:
            self.ammo += amount
            return True  # able to give ammo


